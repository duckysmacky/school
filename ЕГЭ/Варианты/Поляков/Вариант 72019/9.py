file = open("9.txt")

def check(a: int, b: int, c: int) -> bool:
    return (a ** 2 == b ** 2 + b * c + c ** 2) \
        or (b ** 2 == c ** 2 + c * a + a ** 2) \
        or (c ** 2 == a ** 2 + a * b + b ** 2)

cnt = 0
for line in file:
    sides = list(map(int, line.split()))
    if check(sides[0], sides[1], sides[2]) \
            or check(sides[1], sides[2], sides[0]) \
            or check(sides[2], sides[0], sides[1]):
        cnt += 1
print(cnt)