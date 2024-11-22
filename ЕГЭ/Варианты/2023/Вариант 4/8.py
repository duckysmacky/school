from itertools import permutations

def check(word: str) -> bool:
    return word[len(word) // 2 - 1: len(word) // 2 + 1] == "БР"

cnt = 0
for word in set(permutations("АМФИБРАХИЙ")):
    if check(''.join(word)):
        cnt += 1
print(cnt)