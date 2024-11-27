import ipaddress as ip

cnt = 0
mask = "255.255.128.0"
network = ip.ip_network(f"0.0.0.0/{mask}")
for addr in network.hosts():
    if int(f"{addr:b}", 2) % 4 == 0:
        cnt += 1
print(cnt)