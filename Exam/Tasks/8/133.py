from itertools import product

words = list(product("ЗДАНИЕ", repeat=6))
count = 0
for word in words:
    if len(set(word)) == len(word) and all("".join(g) not in "".join(word) for g in list(product("АИЕ", repeat=2))):
        count += 1

print(count)
# 144
