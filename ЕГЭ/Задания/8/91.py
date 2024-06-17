from itertools import product

words = list(product("КАЛИЙ", repeat=5))
count = 0
for word in words:
    if word[0] != "Й" and len(set(word)) == len(word) and "ИА" not in "".join(word):
        count += 1

print(count)
# 78
