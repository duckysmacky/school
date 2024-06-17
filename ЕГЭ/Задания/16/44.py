from functools import lru_cache

def F(n):
    if n <= 3: return n
    if n > 3 and n % 3 == 0: return n * n * n + F(n - 1)
    if n > 3 and n % 3 == 1: return 4 + F(n // 3)
    if n > 3 and n % 3 == 2: return n * n + F(n - 2)
    
print(F(100))
# 121757