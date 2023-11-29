import pytest

from cfcrawler.client import AsyncClient
from cfcrawler.types import Browser


@pytest.mark.asyncio
async def test_crawl():
    client = AsyncClient(browser=Browser.CHROME)
    resp = await client.get("https://www.cloudflare.com/")
    assert resp.status_code == 200
    assert "__cf_bm" in resp.cookies.keys()

    client = AsyncClient(browser=Browser.FIREFOX)
    resp = await client.get("https://www.cloudflare.com/")
    assert resp.status_code == 200
    assert "__cf_bm" in resp.cookies.keys()
