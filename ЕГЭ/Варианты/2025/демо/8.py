from itertools import product

count = 0
for x in product("0123456789AB", repeat=5):
    if x[0] == '0': continue
    num = ''.join(x)
    if num.count('7') == 1 and (num.count('9') + num.count('10') + num.count('A') + num.count('B')) <= 3:
        count += 1
print(count)
