# V2Client - A V2Ray/V2Fly client for python

# Installation

```bash
pip install v2client
```

# Usage (for V2Ray support)

```python
from v2client import V2RayClient, utils

client = V2RayClient("SERVER_IP_ADDRESS", 8080)
usage = client.get_user_usage("email@gmail.com")
print(f"Download Usage: {usage.download}")
print(f"Upload Usage: {usage.upload}")

# Add User
client.add_user(
    inbound_tag="inbound_tag", 
    proxy_type="vless", # VMESS or VLESS
    email="email@gmail.com", 
    level=0,
    user_id=utils.random_uuid()
)

# Remove User
client.remove_user("email@gmail.com")
```

