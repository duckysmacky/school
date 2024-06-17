# TODO
D = range(133, 178)
B = range(144, 191)

m = []
ALL = 500

for start in range(1, ALL):
    for end in range(start, ALL):
        found = True
        for x in range(1, ALL):
            A = range(start, end)
            if (not (x in D) or (not (not (x in B) and not (x in A)) or not (x in D))) == 1: continue
            found = False
            break
        if found: break
    print(start, end)
    m.append(end - start)
        
print(m)
# 11
# correct: 120