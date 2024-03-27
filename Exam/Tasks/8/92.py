from itertools import product

words = list(product("МАНОК", repeat=5))
count = 0
for word in words:
    if word[0] != "О" and len(set(word)) == len(word) and "АО" not in "".join(word):
        count += 1

print(count)
# 72
