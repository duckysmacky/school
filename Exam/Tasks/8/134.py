from itertools import product

words = list(product("ВОРОТА", repeat=6))
count = 0
for word in words:
    if all("".join(g) not in "".join(word) for g in list(product("ОА", repeat=2))):
        print(word)
        count += 1

print(count)
# 15309
