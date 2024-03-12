from itertools import product

words = list(product("ЕИКНУЧ", repeat=3))
count = 0
for index, word in enumerate(words):
    if word[0] == "К":
        print(index)
        break

# 72
