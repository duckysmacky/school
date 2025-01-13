import ipaddress as ip

net = ip.ip_network("192.168.5.0/255.255.255.240")
print(len(list(net.hosts())))
# 14