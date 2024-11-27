import ipaddress as ip

ip1 = "118.222.130.140".split('.')
ip2 = "118.222.201.140".split('.')

print(int(ip1[2]) & int(ip2[2]))