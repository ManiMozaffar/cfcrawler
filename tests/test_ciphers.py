import ssl

import pytest

from cfcrawler.tls import get_cipher_suite
from cfcrawler.types import Browser


def test_valid_ciphers():
    for browser in Browser:
        cipher_suite = get_cipher_suite(browser)
        try:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.set_ciphers(cipher_suite)
        except ssl.SSLError:
            pytest.fail(f"Cipher {cipher_suite} is not supported for {browser}")
