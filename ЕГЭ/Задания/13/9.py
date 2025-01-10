from ipaddress import ip_network, ip_address

def check(num: int) -> bool:
    for n in range(1, 16):
        if 2 ** n - 1 == num:
            return True
    return False

network = ip_network(f"139.75.100.0/255.255.252.0", False)
cnt = 0
for ip in network:
    ip2 = f"{ip:b}"
    last = int(ip2[-8:], 2)
    if check(last):
        cnt += 1
print(cnt)
