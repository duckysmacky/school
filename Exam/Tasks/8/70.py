from itertools import product

words = list(product("АБВГ", repeat=5))
count = 0
for word in words:
    if word.count("Г") <= 1 and word[-1] == "Г":
        print(word)
        count += 1

print(count)
# 81
