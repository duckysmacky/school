N, M = map(int, input().split(' '))
Y = []
for y in range(N): Y.append(input().strip())

def f(x, i):
    try: return x[i] == '#'
    except IndexError: return False

c = 0
for y in range(N):
    print(Y[y])
    lPairs = []
    for x in range(M):
        i = x
        pairs = []
        while f(Y[y], i):
            pairs.append(i)
            i += 1
        if not any([set(pairs).issubset(pair) for pair in lPairs]) and len(pairs) > 0: lPairs.append(pairs)
    print(lPairs)

    for pair in lPairs:
        try: ofsY = Y[y + 1]
        except IndexError: ofsY = Y[y]
        if all([f(ofsY, num) for num in pair]):
            print(f"Pair {pair} works")
            c += 1
        elif len(pair) == 1 and (y == (N - 1) or ofsY[pair[0]] == '.'):
            print(f"Pair {pair} works")
            c += 1
        lPairs.remove(pair)

print()
print(c)
