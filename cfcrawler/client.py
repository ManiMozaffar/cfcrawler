import random
import typing
from functools import lru_cache

from httpx import AsyncHTTPTransport, _types
from httpx._client import AsyncClient as _AsyncClient
from httpx._config import (
    DEFAULT_LIMITS,
    DEFAULT_MAX_REDIRECTS,
    DEFAULT_TIMEOUT_CONFIG,
    Limits,
)
from httpx._transports.base import AsyncBaseTransport
from typing_extensions import assert_never

from cfcrawler.tls import modify_tls_fingerprint
from cfcrawler.types import Browser
from cfcrawler.user_agent import get_all_ua_for_specific_browser


@lru_cache
def get_fake_ua_factory(browser: Browser):
    from fake_useragent import UserAgent

    match browser:
        case Browser.CHROME:
            browsers = ["chrome"]
        case Browser.FIREFOX:
            browsers = ["firefox"]

        case _:
            assert_never(browser)

    ua = UserAgent(browsers=browsers)
    return ua


class AsyncClient(_AsyncClient):
    def __init__(
        self,
        *,
        browser: typing.Optional[Browser] = None,
        default_user_agent: typing.Optional[str] = None,
        cipher_suite: typing.Optional[str] = None,
        ecdh_curve: typing.Optional[str] = None,
        user_agent_factory: typing.Optional[typing.Callable[[], str]] = None,
        use_fake_useragent_library: bool = False,
        transport: typing.Optional[AsyncHTTPTransport] | None = None,
        auth: typing.Optional[_types.AuthTypes] = None,
        params: typing.Optional[_types.QueryParamTypes] = None,
        headers: typing.Optional[_types.HeaderTypes] = None,
        cookies: typing.Optional[_types.CookieTypes] = None,
        verify: _types.VerifyTypes = False,
        cert: typing.Optional[_types.CertTypes] = None,
        http1: bool = True,
        http2: bool = False,
        proxies: typing.Optional[_types.ProxiesTypes] = None,
        mounts: typing.Optional[typing.Mapping[str, AsyncBaseTransport]] = None,
        timeout: _types.TimeoutTypes = DEFAULT_TIMEOUT_CONFIG,
        follow_redirects: bool = False,
        limits: Limits = DEFAULT_LIMITS,
        max_redirects: int = DEFAULT_MAX_REDIRECTS,
        event_hooks: typing.Optional[
            typing.Mapping[str, typing.List[typing.Callable[..., typing.Any]]]
        ] = None,
        base_url: _types.URLTypes = "",
        app: typing.Optional[typing.Callable[..., typing.Any]] = None,
        trust_env: bool = True,
        default_encoding: typing.Union[str, typing.Callable[[bytes], str]] = "utf-8",
    ):
        self.browser: Browser = browser or random.choice(
            [Browser.CHROME, Browser.FIREFOX]
        )
        self.user_agent_factory = user_agent_factory
        self.use_fake_useragent_library = use_fake_useragent_library
        self.default_user_agent = default_user_agent
        self._custom_transport = transport or AsyncHTTPTransport()
        self.ecdh_curve = ecdh_curve
        self.cipher_suite = cipher_suite

        super().__init__(
            auth=auth,
            params=params,
            headers=headers or {},
            cookies=cookies,
            timeout=timeout,
            follow_redirects=follow_redirects,
            max_redirects=max_redirects,
            event_hooks=event_hooks,
            base_url=base_url,
            verify=verify,
            cert=cert,
            http2=http2,
            transport=self._custom_transport,
            app=app,
            http1=http1,
            proxies=proxies,
            limits=limits,
            trust_env=trust_env,
            default_encoding=default_encoding,
            mounts=mounts,
        )
        self.shuffle_user_agent(self.get_random_user_agent())

    def shuffle_user_agent(self, user_agent: str):
        self.headers.update({"User-Agent": user_agent})
        modify_tls_fingerprint(
            pool=self._custom_transport._pool,
            browser=self.browser,
            ecdh_curve=self.ecdh_curve,
            cipher_suite=self.cipher_suite,
        )

    def get_random_user_agent(self) -> str:
        if self.default_user_agent:
            return self.default_user_agent
        elif self.user_agent_factory:
            return self.user_agent_factory()
        elif self.use_fake_useragent_library:
            ua = get_fake_ua_factory(self.browser)
            return typing.cast(str, ua.random)
        else:
            return random.choice(get_all_ua_for_specific_browser(self.browser))
