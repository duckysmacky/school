import ipaddress as ip

net1 = ip.ip_network("192.0.0.0/8")
net2 = ip.ip_network("172.0.0.0/8")

print(list(net1.hosts()))