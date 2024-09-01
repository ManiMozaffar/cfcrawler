import pytest
from httpx import AsyncClient as DetectedClient

from cfcrawler.client import AsyncClient
from cfcrawler.types import Browser


@pytest.mark.asyncio
async def test_patched_async_client():
    client = AsyncClient(browser=Browser.CHROME)
    resp = await client.get("https://www.futbin.com/")
    assert resp.status_code == 200
    assert "__cf_bm" in resp.cookies.keys()

    client = AsyncClient(browser=Browser.FIREFOX)
    resp = await client.get("https://www.futbin.com/")
    assert resp.status_code == 200
    assert "__cf_bm" in resp.cookies.keys()

    client = AsyncClient(browser=Browser.FIREFOX, use_fake_useragent_library=True)
    resp = await client.get("https://www.futbin.com/")
    assert resp.status_code == 200
    assert "__cf_bm" in resp.cookies.keys()


@pytest.mark.asyncio
async def test_of_assumption_tht_target_is_still_protected():
    client = DetectedClient()
    resp = await client.get("https://www.futbin.com/")
    assert resp.status_code != 200
