import grpc # noqa

from api.v2ray.app.log.command import config_pb2 as log_config_pb2, config_pb2_grpc as log_config_pb2_grpc
from v2client import exceptions
from v2client.v2ray import V2RayBase


class LogAPI(V2RayBase):

    def restart_logger(self):
        """
        Restart V2Ray logger.
        :return: None
        """
        stub = log_config_pb2_grpc.LoggerServiceStub(self.channel)
        try:
            stub.RestartLogger(log_config_pb2.RestartLoggerRequest())
        except grpc.RpcError as e:
            exceptions.auto_raise(e)
