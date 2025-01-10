from ipaddress import ip_network, ip_address

addr = ip_address("132.118.34.161")
for m in range(32, 0, -1):
    network = ip_network(f"132.118.34.161/{m}", False)
    cnt = 0
    for ip in network:
        if f"{ip:b}".count('1') == 13:
            cnt += 1
    if cnt == 35:
        print(32 - m)
        break
