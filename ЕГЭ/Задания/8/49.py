from itertools import product

words = list(product("КАТЕР", repeat=3))
count = 0
for word in words:
    if word.count("Р") >= 2:
        count += 1

print(count)
# 13
