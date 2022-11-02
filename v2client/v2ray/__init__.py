import grpc


class V2RayBase:

    def __init__(self, address: str, port: int):
        self.channel = grpc.insecure_channel(f"{address}:{port}")
        self.host = address
        self.port = port

