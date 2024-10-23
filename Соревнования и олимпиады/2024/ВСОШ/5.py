from itertools import product

b = int(input())
n = int(input())
t = int(input())

masks = []
sums = []
for i in range(2 * t):
    if i % 2 == 0:
        masks.append(input())
    else:
        sums.append(int(input()))


def check_code(code: tuple, masks: list, sums: list) -> bool:
    for i in range(t):
        summ_code = 0
        for j in range(len(masks[i])):
            if masks[i][j] == '1':
                summ_code += code[j]
        if summ_code != sums[i]:
            return False
    return True


count = 0
for code in product(range(b), repeat=n):
    if check_code(code, masks, sums):
        count += 1

print(count)