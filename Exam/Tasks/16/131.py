from sys import setrecursionlimit

setrecursionlimit(10 ** 9)

def F(n):
    if n == 1: return 1
    if n > 1: return n * F(n - 1)
    
print(F(2023) / F(2020))
# 8266912626