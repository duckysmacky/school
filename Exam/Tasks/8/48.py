from itertools import product

perms = list(product("БАЛКОН", repeat=5))
count = 0
for word in perms:
    if "Б" in word:
        count += 1

print(count)
# 4651
