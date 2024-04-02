n, k, d = map(int, input().split(' '))
for _ in range(d):
    i = 0
    while not (n * 10 + i) % k == 0:
        if i < 9: i += 1
        else: 
            n = -1
            break
    n = n * 10 + i
print(n)