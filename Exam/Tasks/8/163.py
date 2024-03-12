from itertools import product

a = list(product("13579", repeat=2))
b = list(product("02468", repeat=2))

pairs = []
for a_ in a:
    for b_ in b:
        pairs.append("".join(a_) + "".join(b_))

print(pairs)
count = 0
for x in range(8 ** 7, 8 ** 8):
    num = str(x)
    if len(oct(x)[:2]) == 8 and len(set(num)) == len(num) and all("".join(p) not in num for p in a) and all("".join(p) not in num for p in b):
        print(num)
        count += 1

print(f"Count: {count}")
# 15309
