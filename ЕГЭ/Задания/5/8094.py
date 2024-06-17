def R(N: int):
    num = bin(N)[2:]
    for i in range(2): num += str((sum(list(map(int, num))) % 2))
    return num

for N in range(0, 10_000):
    if int(R(N), 2) > 77: break
    
print(N)
# 19