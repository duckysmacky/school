file = open("9.txt")

def check(x1: int, y1: int, x2: int, y2: int) -> bool:
    crossing = ((x1 > 0) == (x2 < 0)) or ((y1 > 0) == (y2 < 0))
    length = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return crossing and length <= 5  

cnt = 0
for line in file:
    nums = list(map(int, line.split()))
    if check(*nums):
        cnt += 1
print(cnt)