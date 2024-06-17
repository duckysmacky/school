from functools import lru_cache

@lru_cache
def F(n):
    if n <= 3: return n
    if n > 3 and n % 2 == 0: return n + 3 + F(n - 1)
    if n > 3 and n % 2 != 0: return n * n + F(n - 2)

c = 0
for i in range(1, 1001):
    if F(i) % 7 == 0:
        c += 1

print(c)
# 285