file = open("9.txt")

def crosses(a1: int, a2: int, b1: int, b2: int) -> bool:
    return ((a1 > 0) == (a2 > 0)) and ((b1 > 0) != (b2 > 0))


def check(x1: int, y1: int, x2: int, y2: int) -> bool:
    x, y = abs(x1 - x2), abs(y1 - y2)
    length = (x ** 2 + y ** 2) ** 0.5
    cross_cnt = crosses(x1, x2, y1, y2) + crosses(y1, y2, x1, x2)
    return cross_cnt == 1 and length <= 5  


cnt = 0
for line in file:
    nums = list(map(int, line.split()))
    if check(*nums):
        cnt += 1
print(cnt)