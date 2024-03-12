from itertools import product, permutations

words = list(permutations("ВОТОРА"))
vowels = list(product("ОА", repeat=2))

count = 0
for word in words:
    if all("".join(g) not in "".join(word) for g in vowels):
        print(word)
        count += 1

print(count)
# 15309
