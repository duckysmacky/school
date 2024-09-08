P = range(15, 40 + 1)
Q = range(21, 63 + 1)
A = []

for x in range(15, 63 + 1):
    if (not (x in P) or (not ((x in Q) and not (x in A)) or not (x in P))) == False:
        A.append(x)
print(A[-1] - A[0])
