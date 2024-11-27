from itertools import product

cnt = 0
words = [''.join(word) for word in product("АЕПСТУХ", repeat=4)]
for n, word in enumerate(words, start=1):
    if n <= 1000: continue

    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            break
    else:
        cnt += 1
print(cnt)