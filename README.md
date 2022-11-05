# V2Client - A V2Ray/V2Fly client for python

# Installation

```bash
pip install v2client
```

# Usage (for V2Ray support)

```python
from v2client import utils
from v2client import V2RayClient
from v2client import enum as v2types

client = V2RayClient("SERVER_IP_ADDRESS", 8080)
usage = client.get_user_usage("email@gmail.com")
print(f"Download Usage: {usage.download}")
print(f"Upload Usage: {usage.upload}")

# ADD VLESS USER
client.add_user(
    inbound_tag="inbound_tag",
    proxy_type=v2types.ProxyTypes.VLESS,
    email="email@gmail.com",
    level=0,
    flow=v2types.VLESSFlowTypes.XTLS_RPRX_ORIGIN,  # Only for VLESS
    encryption=v2types.VLESSEncryptionTypes.NONE,  # Only for VLESS
    user_id=utils.random_uuid()
)

# ADD VMESS USER
client.add_user(
    inbound_tag="inbound_tag",
    proxy_type=v2types.ProxyTypes.VMESS,
    email="email@email.com",
    level=0,
    security=v2types.VMessSecurityTypes.AES128_GCM,  # Only for VMESS
    user_id=utils.random_uuid()
)

# Remove User
client.remove_user(inbound_tag="inbound", email="email@gmail.com")
```

