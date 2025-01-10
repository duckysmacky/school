from ipaddress import ip_network

network = ip_network("218.194.82.148/255.255.255.192", False)
print(str(list(network.hosts())[-1]).replace('.', ''))
