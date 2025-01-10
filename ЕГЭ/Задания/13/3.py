from ipaddress import ip_network, ip_address

network = ip_network("126.115.78.15/255.255.224.0", False)
cnt = 0
for ip in network:
    if f"{ip:b}".count('1') == 22:
        cnt += 1
print(cnt)
