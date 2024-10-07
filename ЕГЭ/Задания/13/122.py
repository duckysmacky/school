from ipaddress import ip_network

for mask in range(32 + 1):
    net = ip_network(f"106.113.64.105/{mask}", False)
    print(net)