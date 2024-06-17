from functools import lru_cache

@lru_cache
def G(n):
    if n == 1: return 1
    if n > 1: return F(n - 1) + G(n - 1) + n
    
def F(n):
    if n == 1: return 1
    if n > 1: return F(n - 1) - 2 * G(n - 1)

print(G(36))
print(sum(map(int, str(G(36)))))
# 40