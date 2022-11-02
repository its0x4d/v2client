from v2client import V2RayClient, utils

client = V2RayClient("94.182.155.103", 8080)
print(client.get_sys_stats())
print(client.remove_user("inbound", "mosydev2017@gmail.com"))
# print(client.get_user_usage("mosydev2017@gmail.com"))
# uuid = utils.random_uuid()
print(client.add_user(
    inbound_tag="inbound",
    email="mosydev2017@gmail.com",
    proxy_type="vless",
    level=0,
    user_id="93f7d83b-2eff-4f36-b7b0-3bfc23efca46"
))
print("Proxy added")
print(f"vless://93f7d83b-2eff-4f36-b7b0-3bfc23efca46@94.182.155.103:443?path=%2F&security=none&type=ws#Mostafa-Mahan")
