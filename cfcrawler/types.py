from enum import Enum, auto

from typing_extensions import DefaultDict


class StrEnum(str, Enum):
    """
    Enum where members are also (and must be) strings
    """

    def __new__(cls, *values):
        "values must already be of type `str`"
        if len(values) > 3:
            raise TypeError("too many arguments for str(): %r" % (values,))
        if len(values) == 1:
            # it must be a string
            if not isinstance(values[0], str):
                raise TypeError("%r is not a string" % (values[0],))
        if len(values) >= 2:
            # check that encoding argument is a string
            if not isinstance(values[1], str):  # type: ignore
                raise TypeError("encoding must be a string, not %r" % (values[1],))  # type: ignore
        if len(values) == 3:
            # check that errors argument is a string
            if not isinstance(values[2], str):
                raise TypeError("errors must be a string, not %r" % (values[2]))
        value = str(*values)
        member = str.__new__(cls, value)
        member._value_ = value
        return member

    def _generate_next_value_(name, start, count, last_values):  # type: ignore
        """
        Return the lower-cased version of the member name.
        """
        return name.lower()


class ChallengeStatus(StrEnum):
    PASSED = auto()  # dummy value representing a successful attempt
    H_CAPTCHA_V1 = auto()
    H_CAPTCHA_V2 = auto()
    RECAPTCHA = auto()
    IUAM_V1 = auto()
    IUAM_V2 = auto()
    FIREWALL_BLOCKED = auto()

    UNKNOWN = auto()


class CaptchaTypes(StrEnum):
    RE_CAPTCHA = auto()
    H_CAPTCHA = auto()


class ChallengeForm(DefaultDict):
    form: str
    challengeUUID: str


class CaptchaResult(DefaultDict):
    url: str
    data: dict


class Browser(StrEnum):
    CHROME = auto()
    FIREFOX = auto()
