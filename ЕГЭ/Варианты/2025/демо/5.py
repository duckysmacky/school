def R(x: int) -> int:
    num = bin(x)[2:]
    if x % 2 == 0:
        num = f"10{num}"
    else:
        num = f"1{num}01"
    return int(num, 2)


max_R = 0
for N in range(13):
    max_R = max(max_R, R(N))
print(max_R)
