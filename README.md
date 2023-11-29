# cfcrawler

[![Release](https://img.shields.io/github/v/release/ManiMozaffar/cfcrawler)](https://img.shields.io/github/v/release/ManiMozaffar/cfcrawler)
[![Build status](https://img.shields.io/github/actions/workflow/status/ManiMozaffar/cfcrawler/main.yml?branch=main)](https://github.com/ManiMozaffar/cfcrawler/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/ManiMozaffar/cfcrawler/branch/main/graph/badge.svg)](https://codecov.io/gh/ManiMozaffar/cfcrawler)
[![Commit activity](https://img.shields.io/github/commit-activity/m/ManiMozaffar/cfcrawler)](https://img.shields.io/github/commit-activity/m/ManiMozaffar/cfcrawler)
[![License](https://img.shields.io/github/license/ManiMozaffar/cfcrawler)](https://img.shields.io/github/license/ManiMozaffar/cfcrawler)

Cloudflare scraper and cralwer written in Async, In-place library for HTTPX.
Crawl website that has cloudflare enabled, easier than ever!

- **Github repository**: <https://github.com/ManiMozaffar/cfcrawler/>

## Getting started

To use library, simply replace your aiohttp client with ours!

```python
from cfcrawler import AsyncClient

async def get(url):
    client = AsyncClient()
    await client.get(url)

```

You can also rotate user agents

```python
from cfcrawler import AsyncClient

client = AsyncClient()
client.rotate_useragent()
```

You can also specify which browser you want to use
```python
from cfcrawler.types import Browser
from cfcrawler import AsyncClient

AsyncClient(browser=Browser.CHROME)
```

You can also use asyncer to syncify the implementation
```python
from cfcrawler import AsyncClient
from asyncer import syncify

def get(url):
    client = AsyncClient()
    syncify(client.get)(url)
```

## Coming Next

1. CF JS Challenge solver
2. Captcha solver integration (2Captcha and etc)


## Contribution

I'll work on this library in few months, I don't have free time right now, but feel free to contribute.
I'll check and test the PRs myself!
