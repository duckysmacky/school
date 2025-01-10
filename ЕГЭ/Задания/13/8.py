from ipaddress import ip_network, ip_address

for A in range(0, 256):
    network = ip_network(f"159.242.{A}.223/255.255.254.0", False)
    for ip in network:
        ip2 = f"{ip:b}"
        left = ip2[:16].count('0')
        right = ip2[16:].count('0')
        if not (left < right):
            break
    else:
        print(A)
