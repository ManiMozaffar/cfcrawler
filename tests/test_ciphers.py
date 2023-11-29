import ssl

import pytest

from cfcrawler.cipher import MAP_BROWSER_TO_CIPHER


def test_valid_ciphers():
    for browser, ciphers in MAP_BROWSER_TO_CIPHER.items():
        cipher_suite = ":".join(ciphers)
        try:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.set_ciphers(cipher_suite)
        except ssl.SSLError:
            pytest.fail(f"Cipher {cipher_suite} is not supported for {browser}")
