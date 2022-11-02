import grpc

from v2client import exceptions
from v2client.v2ray import V2RayBase
from api.v2ray.app.proxyman.command import command_pb2, command_pb2_grpc
from api.v2ray.common.protocol import user_pb2
from api.v2ray.proxy.vless import account_pb2 as vless_account_pb2
from api.v2ray.proxy.vmess import account_pb2 as vmess_account_pb2
from v2client.utils import to_typed_message


class ProxyAPI(V2RayBase):

    @staticmethod
    def _vless_account_validator(user_id: str, flow: str = None, encryption: str = None) -> vless_account_pb2.Account:
        """
        Validate VLESS config
        :param user_id: user UUID
        :param flow: flow type
        :param encryption: encryption type
        :return: VLESS account
        """
        if flow and flow not in ["xtls-rprx-direct", "xtls-rprx-origin", "xtls-rprx-splice"]:
            raise ValueError(f"Invalid flow: {flow}")
        if encryption and encryption not in [
            "none", "xsalsa20-poly1305", "chacha20-poly1305", "chacha20-ietf-poly1305"
        ]:
            raise ValueError(f"Invalid encryption: {encryption}")

        return vless_account_pb2.Account(
            id=user_id,
            flow=flow,
            encryption=encryption
        )

    @staticmethod
    def _vmess_account_validator(user_id: str, alter_id: int, security: str = None) -> vmess_account_pb2.Account:
        """
        Validate VMess config
        :param user_id: user UUID
        :param alter_id: alter ID
        :param security: security type
        :return: VMess account
        """
        if security and security not in ["auto", "aes-128-gcm", "chacha20-poly1305", "none"]:
            raise ValueError(f"Invalid security: {security}")

        return vmess_account_pb2.Account(
            id=user_id,
            alter_id=alter_id or 0,
            security=security or "auto"
        )

    def add_user(self, inbound_tag: str, email: str, proxy_type: str, level: int, **kwargs):
        """
        Add a user to an inbound.

        :param inbound_tag: Inbound tag
        :param email: User email
        :param proxy_type: Proxy type (vmess, vless)
        :param level: User level
        :param kwargs: Keyword arguments
        :return: None
        """
        stub = command_pb2_grpc.HandlerServiceStub(self.channel)
        if proxy_type == "vless":
            account = self._vless_account_validator(**kwargs)
        elif proxy_type == "vmess":
            account = self._vmess_account_validator(**kwargs)
        else:
            raise exceptions.InvalidProxyType(proxy_type)

        try:
            stub.AlterInbound(command_pb2.AlterInboundRequest(
                tag=inbound_tag,
                operation=to_typed_message(command_pb2.AddUserOperation(
                    user=user_pb2.User(
                        email=email,
                        level=level,
                        account=to_typed_message(account)
                    )
                ))
            ))
        except grpc.RpcError as e:
            if "already exists" in e.details():
                raise exceptions.UserAlreadyExists(email)
            raise e

    def remove_user(self, inbound_tag: str, email: str):
        """
        Remove a user from an inbound.
        :param inbound_tag: The tag of the inbound.
        :param email: The email of the user.
        :return: None
        """
        stub = command_pb2_grpc.HandlerServiceStub(self.channel)
        stub.AlterInbound(command_pb2.AlterInboundRequest(
            tag=inbound_tag,
            operation=to_typed_message(command_pb2.RemoveUserOperation(
                email=email
            ))
        ))

