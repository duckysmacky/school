from functools import lru_cache

@lru_cache
def F(n):
    if n == 1: return 1
    if n > 1: return F(n - 1) + 3 * G(n - 1)
    
def G(n):
    if n == 1: return 1
    if n > 1: return F(n - 1) - 2 * G(n - 1)
    
print(sum(map(int, str(F(18)))))
# 46