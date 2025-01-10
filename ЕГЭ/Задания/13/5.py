from ipaddress import ip_network, ip_address

network = ip_network("94.253.128.0/255.255.128.0", False)
cnt = 0
for ip in network:
    ip2 = f"{ip:b}"
    if ip2.count('1') % 6 != 0 and ip2[-3:] == "101":
        cnt += 1
print(cnt)
