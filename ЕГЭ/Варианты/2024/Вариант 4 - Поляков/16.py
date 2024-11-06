from functools import lru_cache


@lru_cache
def f(n):
    if n == 0: return 0
    if n > 0 and n % 2 == 0: return f(n / 2) - 1
    if n > 0 and n % 2 != 0: return 1 + f(n - 1)

cnt = 0
for n in range(0, 1000):
    if f(n) == 0:
        cnt += 1
print(cnt)