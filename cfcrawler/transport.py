import ssl

from httpx import AsyncHTTPTransport

from cfcrawler.cipher import MAP_BROWSER_TO_CIPHER
from cfcrawler.types import Browser


class CfScrapeTransport(AsyncHTTPTransport):
    def __init__(
        self,
        browser: Browser,
        ecdh_curve: str | None = None,
        cipher_suite: str | None = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        ecdh_curve = ecdh_curve or "secp384r1"
        map_browser_choice = MAP_BROWSER_TO_CIPHER[browser]
        cipher_suite = cipher_suite or ":".join(map_browser_choice)
        assert (
            self._pool._ssl_context
        ), "SSL Context does not exists in the HTTPX connection pool"
        self._pool._ssl_context.set_ecdh_curve(ecdh_curve)
        self._pool._ssl_context.set_ciphers(cipher_suite)
        self._pool._ssl_context.check_hostname = False

        self._pool._ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2
        self._pool._ssl_context.maximum_version = ssl.TLSVersion.TLSv1_3
        self._pool._ssl_context = self._pool._ssl_context
