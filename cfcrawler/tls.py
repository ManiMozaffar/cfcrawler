import ssl
import typing

from httpcore import AsyncConnectionPool, AsyncHTTPProxy, AsyncSOCKSProxy

from cfcrawler.cipher import MAP_BROWSER_TO_CIPHER
from cfcrawler.types import Browser


def modify_tls_fingerprint(
    pool: AsyncConnectionPool | AsyncHTTPProxy | AsyncSOCKSProxy,
    browser: Browser,
    ecdh_curve: typing.Optional[str] = None,
    cipher_suite: typing.Optional[str] = None,
):
    ecdh_curve = ecdh_curve or "secp384r1"
    map_browser_choice = MAP_BROWSER_TO_CIPHER[browser]
    cipher_suite = cipher_suite or ":".join(map_browser_choice)
    assert pool._ssl_context, "SSL Context does not exists in the HTTPX connection pool"
    pool._ssl_context.set_ecdh_curve(ecdh_curve)
    pool._ssl_context.set_ciphers(cipher_suite)
    pool._ssl_context.check_hostname = False

    pool._ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2
    pool._ssl_context.maximum_version = ssl.TLSVersion.TLSv1_3
    pool._ssl_context = pool._ssl_context
