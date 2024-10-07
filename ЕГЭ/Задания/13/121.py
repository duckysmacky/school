from ipaddress import ip_network

for mask in range(32 + 1):
    net = ip_network(f"133.57.64.130/{mask}", False)
    print(net)