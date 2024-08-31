from functools import lru_cache

from typing_extensions import assert_never

from cfcrawler.types import Browser


@lru_cache
def get_operating_systems() -> list[str]:
    operating_systems = [
        "Windows NT 10.0; Win64; x64",
        "Windows NT 10.0; WOW64",
        "Windows NT 6.1; Win64; x64",
        "Macintosh; Intel Mac OS X 12.4",
        "Macintosh; Intel Mac OS X 10.15",
        "X11; Ubuntu; Linux x86_64",
        "X11; Fedora; Linux x86_64",
    ]
    return operating_systems


def get_all_chrome_ua() -> list[str]:
    operating_systems = get_operating_systems()
    chrome_versions = [
        "115.0.5790.102",
        "114.0.5735.198",
        "113.0.5672.126",
        "112.0.5615.137",
        "111.0.5563.110",
    ]
    return [
        f"Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36"
        for os in operating_systems
        for version in chrome_versions
    ]


def get_all_fireox_ua() -> list[str]:
    operating_systems = get_operating_systems()
    firefox_versions = ["115.0", "114.0", "113.0", "112.0", "111.0", "110.0", "109.0"]
    return [
        f"Mozilla/5.0 ({os}) Gecko/20100101 Firefox/{version}"
        for os in operating_systems
        for version in firefox_versions
    ]


def get_all_ua_for_specific_browser(browser: Browser) -> list[str]:
    match browser:
        case Browser.CHROME:
            return get_all_chrome_ua()
        case Browser.FIREFOX:
            return get_all_fireox_ua()
        case _:
            assert_never(browser)
