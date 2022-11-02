from api.v2ray.common.protocol import user_pb2
from api.v2ray.proxy.vless.inbound import config_pb2 as vless_inbound_config_pb2
from api.v2ray.proxy.vless.outbound import config_pb2 as vless_outbound_config_pb2
from api.v2ray.proxy.vless import account_pb2 as vless_account_pb2
from api.v2ray.proxy.vmess.inbound import config_pb2 as vmess_inbound_config_pb2
from api.v2ray.proxy.vmess.outbound import config_pb2 as vmess_outbound_config_pb2
from api.v2ray.proxy.vmess import account_pb2 as vmess_account_pb2


class BaseProxy:
    def __init__(self):
        self.message = None


class VLessInBound(BaseProxy):

    def __init__(self, *users: dict):
        super(VLessInBound).__init__()
        self.message = vless_inbound_config_pb2.Config(
            clients=[user_pb2.User(
                email=user['email'],
                level=user['level'],
                account=vless_account_pb2.Account(
                    id=user['id'],
                    flow=user['flow']
                )
            ) for user in users]
        )

    def __str__(self):
        return str(self.message)


class VLessOutBound(BaseProxy):

    def __init__(self, *users: dict):
        super(VLessOutBound).__init__()
        self.message = vless_outbound_config_pb2.Config(
            clients=[user_pb2.User(
                email=user['email'],
                level=user['level'],
                account=vless_account_pb2.Account(
                    id=user['id'],
                    flow=user['flow']
                )
            ) for user in users]
        )

    def __str__(self):
        return str(self.message)


class VMessInBound(BaseProxy):

    def __init__(self, *users: dict):
        super(VMessInBound).__init__()
        self.message = vmess_inbound_config_pb2.Config(
            clients=[user_pb2.User(
                email=user['email'],
                level=user['level'],
                account=vmess_account_pb2.Account(
                    id=user['id'],
                    alter_id=user['alter_id'],
                    security=user['security']
                )
            ) for user in users]
        )

    def __str__(self):
        return str(self.message)


class VMessOutBound(BaseProxy):

    def __init__(self, *users: dict):
        super(VMessOutBound).__init__()
        self.message = vmess_outbound_config_pb2.Config(
            clients=[user_pb2.User(
                email=user['email'],
                level=user['level'],
                account=vmess_account_pb2.Account(
                    id=user['id'],
                    alter_id=user['alter_id'],
                    security=user['security']
                )
            ) for user in users]
        )

    def __str__(self):
        return str(self.message)
