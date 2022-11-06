from v2client.v2ray.log import LogAPI
from v2client.v2ray.proxy import ProxyAPI
from v2client.v2ray.stats import StatsAPI


class V2RayClient(ProxyAPI, StatsAPI, LogAPI):
    """
    V2Ray Client API
    """
    pass
