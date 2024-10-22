import ipaddress as ip

ipaddr = ip.ip_address("172.49.54.172")
ipnet = ip.ip_network("172.49.48.0")

print(ipnet.prefixlen)