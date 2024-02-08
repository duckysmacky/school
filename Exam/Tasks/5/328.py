def R(N):
    n = bin(N)[2:]
    if N % 5 == 0:
        n = "1" + n + n[-2:]
    else:
        n = bin(N % 5)[2:] + n
    
    return int(n, 2)

r = {}

for N in range(1, 10_000):
    if R(N) <= 223:
        r[N] = R(N)
        
print(max(r.values())) # 219