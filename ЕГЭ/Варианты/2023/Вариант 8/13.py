def ip(ip: str) -> list:
    return list(map(lambda x: int(x), ip.split('.')))

addr = ip("91.62.203.130")
net = ip("91.62.192.0")
print(addr)
print(net)
print([bin(x)[2:] for x in addr])
print([bin(x)[2:] for x in net])
mask = [addr[i] & net[i] for i in range(4)]
print(sum(map(lambda x: bin(x)[2:].count('1'), mask)))