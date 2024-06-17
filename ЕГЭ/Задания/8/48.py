from itertools import product

words = list(product("БАЛКОН", repeat=5))
count = 0
for word in words:
    if "Б" in word:
        count += 1

print(count)
# 4651
