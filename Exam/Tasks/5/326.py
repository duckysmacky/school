def R(N):
    n = str(bin(N))[2:]
    if N % 2 == 0:
        n = "1" + n + n[-1]
    else:
        n = n + "0" + n[-1]
    return int(n, 2)

r = {}

for N in range(1, 10_000):
    if R(N) > 100:
        r[R(N)] = N
        
print(r[min(r.keys())]) # 25