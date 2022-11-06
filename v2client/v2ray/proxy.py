import grpc  # noqa

from api.v2ray.app.proxyman.command import command_pb2, command_pb2_grpc
from api.v2ray.common.protocol import user_pb2
from api.v2ray.common.protocol.headers_pb2 import SecurityConfig
from api.v2ray.proxy.vless import account_pb2 as vless_account_pb2
from api.v2ray.proxy.vmess import account_pb2 as vmess_account_pb2
from v2client import enum as v2types
from v2client import exceptions
from v2client.utils import to_typed_message
from v2client.v2ray import V2RayBase


class ProxyAPI(V2RayBase):

    @staticmethod
    def _vless_account_validator(
            user_id: str,
            flow: str = None,
            encryption: str = None
    ) -> vless_account_pb2.Account:
        """
        Validate VLESS config
        :param user_id: user UUID
        :param flow: flow type
        :param encryption: encryption type
        :return: VLESS account
        """
        if flow and flow not in v2types.VLESSFlowTypes.__dict__.values():
            raise ValueError(f"Flow '{flow}' is not a valid VLESS flow type.")
        if encryption and encryption not in v2types.VLESSEncryptionTypes.__dict__.values():
            raise ValueError(f"Encryption '{encryption}' is not a valid VLESS encryption type.")

        return vless_account_pb2.Account(
            id=user_id,
            flow=flow,
            encryption=encryption
        )

    @staticmethod
    def _vmess_account_validator(
            user_id: str,
            alter_id: int = 0,
            security: str = v2types.VMessSecurityTypes.AUTO
    ) -> vmess_account_pb2.Account:
        """
        Validate VMESS config
        :param user_id: user UUID
        :param alter_id: alter ID
        :param security: security type
        :return: VMESS account
        """
        if security and security not in v2types.VMessSecurityTypes.__dict__.values():
            raise ValueError(f"Security '{security}' is not a valid VMESS security type.")

        return vmess_account_pb2.Account(
            id=user_id,
            alter_id=alter_id,
            security_settings=SecurityConfig(type=security)
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
        if proxy_type == v2types.ProxyTypes.VLESS:
            account = self._vless_account_validator(**kwargs)
        elif proxy_type == v2types.ProxyTypes.VMESS:
            account = self._vmess_account_validator(**kwargs)
        else:
            raise exceptions.InvalidProxyType(proxy_type=proxy_type)

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
            exceptions.auto_raise(e)

    def remove_user(self, inbound_tag: str, email: str):
        """
        Remove a user from an inbound.
        :param inbound_tag: The tag of the inbound.
        :param email: The email of the user.
        :return: None
        """
        stub = command_pb2_grpc.HandlerServiceStub(self.channel)
        try:
            stub.AlterInbound(command_pb2.AlterInboundRequest(
                tag=inbound_tag,
                operation=to_typed_message(command_pb2.RemoveUserOperation(
                    email=email
                ))
            ))
        except grpc.RpcError as e:
            exceptions.auto_raise(e)
