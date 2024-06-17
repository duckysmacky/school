from functools import lru_cache

@lru_cache
def F(n):
    if n <= 1: return 0
    if n > 1 and n % 2 != 0: return F(n - 1) + 3 * n ** 2
    return n / 2 + F(n - 1) + 2

print(F(49))
# 62820