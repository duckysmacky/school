from ipaddress import *

count = 0
network = ip_network("172.16.168.0/255.255.248.0")
for ip in network:
    ones = 0
    for num in str(ip).split('.'):
        ones += bin(int(num))[2:].count('1')
    if ones % 5 != 0:
        count += 1
print(count)
