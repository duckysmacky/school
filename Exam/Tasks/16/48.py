from functools import lru_cache

@lru_cache
def F(n):
    if n <= 3: return n
    if n > 3 and n % 2 == 0: return 2 * n + F(n - 1)
    if n > 3 and n % 2 != 0: return n * n + F(n - 2)

c = 0
for i in range(1, 1000):
    if F(i) < 10 ** 8:
        c += 1

print(c)
# 842