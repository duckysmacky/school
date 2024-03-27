from itertools import product

words = list(product("МУХА", repeat=5))
count = 0
for word in words:
    if word.count("У") <= 3:
        count += 1

print(count)
# 1008
