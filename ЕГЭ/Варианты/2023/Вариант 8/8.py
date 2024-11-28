from itertools import permutations

def check(num: str) -> bool:
    return (len([x for x in num if int(x) % 2 == 0]) == 3) \
        + (len([x for x in num if int(x) % 2 != 0]) == 2) == 1

cnt = 0
for num in permutations("0123456789", r=6):
    num = ''.join(num)
    if num[-2:] == "34" and check(num):
        cnt += 1
print(cnt)