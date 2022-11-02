class UserNotFound(Exception):
    def __init__(self, email):
        super().__init__(f"User {email} not found")


class UserAlreadyExists(Exception):
    def __init__(self, email):
        super().__init__(f"User {email} already exists")


class SocketClosed(Exception):
    """Raised when the config is not supported by the system."""
    pass


class InvalidProxyType(Exception):
    """Raised when the config is not supported by the system."""

    def __init__(self, proxy_type):
        super().__init__(f"Invalid proxy type {proxy_type}")
