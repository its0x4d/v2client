# V2Client - A V2Ray server management for python

## Installation

```bash
pip install v2client
```

## How Activate gRPC API?

```json lines
// Add The following json to your config.json file 
{
  "stats": {},
  "api": {
    "tag": "api",
    "services": [
      "StatsService", // For stats
      "HandlerService", // For User and Inbound management
      "LoggerService" // For log management
    ]
  },
  "policy": {
    "levels": {
      "0": {
        "statsUserUplink": true, // User uplink stats
        "statsUserDownlink": true // User downlink stats
      }
    },
    "system": {
      "statsInboundUplink": true,
      "statsInboundDownlink": true,
      "statsOutboundUplink": true,
      "statsOutboundDownlink": true
    }
  }, 
    // and then add the following inbound
  "inbounds": [
      // ... (other inbounds)
      { 
        "listen": "0.0.0.0",
        "port": 8080, // or any other port you want
        "protocol": "dokodemo-door",
        "settings": {
          "address": "0.0.0.0"
        },
        "tag": "api"
      }
  ],
// and then add the following routing rule
  "routing": {
    "rules": [
      // ... (other rules)
      {
        "inboundTag": [
          "api"
        ],
        "outboundTag": "api",
        "type": "field"
      }
    ],
    "domainStrategy": "AsIs"
  }
}
```

## Usage

```python
from v2client import utils
from v2client import V2RayClient
from v2client import enum as v2types

client = V2RayClient("SERVER_IP_ADDRESS", 8080)
usage = client.get_user_usage("email@gmail.com")
print(f"Download Usage: {usage.download} & Upload Usage: {usage.upload} (in bytes)")

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

