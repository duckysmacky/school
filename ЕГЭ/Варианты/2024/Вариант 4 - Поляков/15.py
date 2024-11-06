P = range(5, 108 + 1)
Q = range(28, 40 + 1)
R = range(16, 72 + 1)

lens = []
for j in range(108 + 1):
    for i in range(j + 1):
        A = range(i, j + 1)
        found = True
        for x in range(1000):
            if not ((not (x in P) or (x in Q)) or ((x in A) or not (x in R))):
                found = False
        if found:
            lens.append(len(A))

print(min(lens))