# cfcrawler

[![Release](https://img.shields.io/github/v/release/ManiMozaffar/cfcrawler)](https://img.shields.io/github/v/release/ManiMozaffar/cfcrawler)
[![Build status](https://img.shields.io/github/actions/workflow/status/ManiMozaffar/cfcrawler/main.yml?branch=main)](https://github.com/ManiMozaffar/cfcrawler/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/ManiMozaffar/cfcrawler/branch/main/graph/badge.svg)](https://codecov.io/gh/ManiMozaffar/cfcrawler)
[![Commit activity](https://img.shields.io/github/commit-activity/m/ManiMozaffar/cfcrawler)](https://img.shields.io/github/commit-activity/m/ManiMozaffar/cfcrawler)
[![License](https://img.shields.io/github/license/ManiMozaffar/cfcrawler)](https://img.shields.io/github/license/ManiMozaffar/cfcrawler)

Cloudflare scraper and cralwer written in Async, In-place library for HTTPX. Crawl website that has cloudflare enabled, easier than ever!

This library is a HTTP client designed to crawl websites protected by Cloudflare, even when their bot detection system is active. If you're already using httpx, you can switch to this library easily since it's a drop-in replacement. Just change the import, and you're good to go.

- **Github repository**: <https://github.com/ManiMozaffar/cfcrawler/>

## Installation

To install base package, you can do:

```bash
pip install cfcrawler
```

To install `fake-useragent` backend support to rotate user agents, you can do:

```bash
pip install "cfcrawler[ua]"
```

## Getting started

To use library, simply replace your aiohttp client with ours! It's completely in-place :)

```python
from cfcrawler import AsyncClient

async def get(url):
    client = AsyncClient()
    await client.get(url)

```

By default, we're using one random user agent, which is still undetected in tests.
To rotate user agent, you need to explicitly call `rotate_useragent` method.
By default, we have a pool of few user agents, But you can also install extra optional dependencies to have a big pool of user agents to rotate between them.

```python
from cfcrawler import AsyncClient

client = AsyncClient(use_fake_useragent_library=True) # one random user agent is selected
# do something
client.rotate_useragent() # user agent is rotated
# do something
client.rotate_useragent() # user agent is rotated again
# do something
```

You can also specify which browser you want to use

```python
from cfcrawler.types import Browser
from cfcrawler import AsyncClient

AsyncClient(browser=Browser.CHROME)
```

If you wish to have your own user agent pool, you can pass the factory callable to the client

```python
from cfcrawler import AsyncClient

def my_useragent_factory():
    return "My User Agent" # your implementation

client = AsyncClient(user_agent_factory=my_useragent_factory)
```

You can also use asyncer to syncify the implementation

```python
from cfcrawler import AsyncClient
from asyncer import syncify

def get(url):
    client = AsyncClient()
    syncify(client.get)(url)
```

## How this library works

### The Problem

Websites using Cloudflare often rely on a bot detection mechanism that works by checking your TLS Fingerprint. So, what's a TLS Fingerprint? When you connect to a website that uses HTTPS, the first thing that happens is the exchange of a "Client Hello" message. This message tells the server some basic info about your client, like the TLS version you support and a list of cipher suites, and etc.

### What's a Cipher Suite?

A cipher suite is a set of cryptographic algorithms that the client and server use to establish a secure connection. Each browser or client has its own specific list of cipher suites, and their order is unique. For instance, Chrome has its own list, Firefox has another, and Python's requests library has a completely different one.

### The Detection

Cloudflare figures out if you're not a real browser by comparing your TLS Fingerprint—which is a combination of the TLS version and cipher suite order—with your user-agent. If there's a mismatch, like if your user-agent says you're Chrome but your cipher suites suggest you're a Python script, Cloudflare knows you're not a browser and blocks the request.

### How My Library Helps

This library handles that problem by aligning your TLS Fingerprint with your user-agent, making it harder for Cloudflare to detect that you're not a real browser. The best part? It's just 10 lines of code! In source code, checkout `cfcrawler/tls.py` to see how it works.

## Coming Next

1. CF JS Challenge solver
2. Captcha solver integration (2Captcha and etc)
