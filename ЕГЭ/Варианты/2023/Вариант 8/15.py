def D(n: int, m: int) -> bool:
    return n % m == 0

for A in range(1, 100_000):
    f = not (not D(396, A) or not D(180, A))
    if f:
        print(A)