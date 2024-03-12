from itertools import product


def check(num: str):
    for i in range(len(num) - 1):
        if not (int(num[i]) % 2 == 0) == (int(num[i + 1]) % 2 != 0):
            return False
    return True


count = 0
for x in range(8 ** 7, 8 ** 8):
    num = oct(x)[2:]
    if len(set(num)) == len(num) and check(num):
        print(num)
        count += 1

print(f"Count: {count}")
# 1008
