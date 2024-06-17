from sys import setrecursionlimit

setrecursionlimit(10 ** 9)

def F(n):
    if n < 7: return 7
    if n >= 7: return n + 1 + F(n - 2)
    
print(F(2024) - F(2020))
# 6069