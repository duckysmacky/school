def add(i, x, y):
    i[0] += x
    i[1] += y
    return i

c = 0
start = [0, 0]
ans = []
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        t = start.copy()
        add(t, -3, 4)
        for i in range(4):
            add(t, a, b)
            add(t, 12, 5)
        add(t, -9, 32)
        if t == start:
            ans = [a, b]
            break
        
print(c)