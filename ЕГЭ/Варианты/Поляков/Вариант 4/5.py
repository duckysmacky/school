def alg(n):
    n2 = bin(n)[2:]
    if n2.count('1') > n2.count('0'):
        n2 += '1'
    else:
        n2 += '0'
    return int(n2, 2)

vals = []
for n in range(1000):
    R = alg(n)
    if R > 40: vals.append(R)
print(min(vals))