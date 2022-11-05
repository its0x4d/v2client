import re


class UserNotFound(Exception):
    pass


class UserAlreadyExists(Exception):
    pass


class UnkownError(Exception):
    pass


class InvalidProxyType(Exception):
    """Raised when the config is not supported by the system."""

    def __init__(self, proxy_type: str):
        super().__init__(f"Invalid proxy type: '{proxy_type}'. Supported types: 'vmess', 'vless'")


class InboundNotFound(Exception):
    """Raised when the config is not supported by the system."""

    def __init__(self, inbound_tag: str):
        super().__init__(f"Inbound '{inbound_tag}' not found")


def auto_raise(e) -> None:
    """
    Raise an exception based on the error message.
    :param e: gRPC error
    :return: None
    :raises: UserNotFound, UserAlreadyExists, UnkownError, InboundNotFound
    """
    user_not_found = [
        re.compile(r"app/stats/command: user>>>.+>>>traffic>>>.+ not found."),
        re.compile(r"proxy/.*: User .* not found."),
    ]
    if "inbound: handler not found:" in e.details():
        raise InboundNotFound(e.details().split(":")[-1].strip())
    elif any(regex.search(e.details()) for regex in user_not_found):
        raise UserNotFound(e.details().split(":")[-1].strip())
    elif "already exists" in e.details():
        raise UserAlreadyExists(e.details().split(":")[-1].strip())
    else:
        raise UnkownError(e.details())
