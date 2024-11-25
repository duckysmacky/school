import ipaddress as ip

ip1 = "118.222.130.140".split('.')
ip2 = "118.222.201.140".split('.')

print(list(map(lambda x: bin(int(x[2]))[2:], [ip1, ip2])))
print(int("01000000", 2))