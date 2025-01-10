from ipaddress import ip_network, ip_address

network = ip_network("102.141.0.0/255.255.192.0", False)
cnt = 0
for ip in network:
    ip2 = f"{ip:b}"
    if ip2.count('1') % 7 == 0 and ip2[-4:] == "1011":
        cnt += 1
print(cnt)
