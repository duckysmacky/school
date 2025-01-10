from ipaddress import ip_network

network = ip_network("135.13.142.29/255.255.255.128", False)
print(str(list(network.hosts())[-1]).replace('.', ''))
