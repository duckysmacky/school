from ipaddress import ip_network, ip_address

network = ip_network("202.75.38.176/255.255.255.240", False)
cnt = 0
for ip in network:
    ip2 = f"{ip:b}"
    if "111" not in ip2 and "000" not in ip2:
        cnt += 1
print(cnt)
