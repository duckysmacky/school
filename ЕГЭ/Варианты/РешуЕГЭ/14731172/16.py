import sys
sys.setrecursionlimit = 100000000

def F(n):
    if n == 0 or n >= 10**9:
        return 0
    elif n % 2 != 0:
        return F(n - 1) + 1
    elif n > 0 and n % 2 == 0:
        return F(n / 2)

count = 0
for n in range(10000000):
    if F(n) == 3:
        count += 1
print(count)