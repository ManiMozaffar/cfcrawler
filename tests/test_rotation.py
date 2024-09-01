import pytest

from cfcrawler.client import AsyncClient
from cfcrawler.types import Browser


@pytest.mark.asyncio
async def test_factory_works():
    ua_pool = ["Mozilla/5.0", "Mozilla/6.0"]
    client = AsyncClient(
        browser=Browser.CHROME, user_agent_factory=lambda: ua_pool.pop()
    )
    assert client.headers["User-Agent"] == "Mozilla/6.0"
    client.rotate_useragent()
    assert client.headers["User-Agent"] == "Mozilla/5.0"


@pytest.mark.asyncio
async def test_rotate_works_with_fake_lib():
    # This test is a bit flaky, but it's good enough for now.
    client = AsyncClient(browser=Browser.CHROME, use_fake_useragent_library=True)
    user_agents: set[str] = set()
    for _ in range(10):
        user_agent_one = client.headers["User-Agent"]
        client.rotate_useragent()
        user_agents.add(user_agent_one)

    assert len(user_agents) > 1  # might have repeated user agents
