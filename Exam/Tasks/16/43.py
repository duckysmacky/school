from functools import lru_cache

def F(n):
    if n <= 3: return n
    if 3 < n and n <= 32: return n // 4 + F(n - 3)
    if n > 32: return 2 * F(n - 5)
    
print(F(100))
# 655360