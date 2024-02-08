def R(N):
    n = str(bin(N))[2:]
    if int(n.count("1")) % 4 == 0:
        n = "10" + n
    else:
        n = "11" + n
    if n[-1] == "0":
        n += "1"
    else:
        n += "0"
    
    return int(n, 2)

r = {}

for N in range(1, 10_000):
    if R(N) <= 250:
        r[N] = R(N)
        
print(r[max(r.keys())]) # 189