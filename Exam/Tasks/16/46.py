from sys import setrecursionlimit

setrecursionlimit(10 ** 5)

def F(n):
    if n <= 3: return n
    if n % 2 == 0 and n > 3: return 2 * n * n + F(n - 1)
    if n % 2 != 0 and n > 3: return n * n * n + n + F(n - 1)
    
c = 0
for i in range(1, 1000):
    f = F(i)
    if f < 10 ** 7:
        c += 1

print(c)
# 92