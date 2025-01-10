from ipaddress import ip_network, ip_address

for m in range(32, -1, -1):
    network = ip_network(f"156.38.155.174/{m}", False)
    cnt = 0
    for ip in network:
        ip2 = f"{ip:b}"
        if ip2.count('1') == 12:
            cnt += 1
    if cnt == 45:
        mask = "1" * m + "0" * (32 - m)
        print(mask, mask.count('1'))
        break
