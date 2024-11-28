def alg(n: int) -> int:
    n2 = bin(n)[2:]
    n2 += "00" if n % 2 == 0 else "10"
    return int(n2, 2)

for n in range(1000):
    R = alg(n)
    if R > 130:
        print(n)
        break