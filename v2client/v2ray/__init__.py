import grpc # noqa


class V2RayBase:
    """
    V2Ray API base class.
    Note: This class is not intended to be used directly.
    GitHub: https://github.com/v2ray/v2ray-core
    """
    def __init__(self, address: str, port: int):
        self.channel = grpc.insecure_channel(f"{address}:{port}")
        self.host = address
        self.port = port

