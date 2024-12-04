from itertools import permutations

def check(num: str) -> bool:
    return (sum(int(x) % 2 == 0 for x in num) == 3) + (sum(int(x) % 2 != 0 for x in num) == 2) == 1

cnt = 0
for num in permutations("0123456789", r=6):
    num = ''.join(num)
    if num[0] != '0' and num[-2:] == "34" and check(num):
        cnt += 1
print(cnt)