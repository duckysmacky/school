r = range(2)

for a in r:
    for b in r:
        for c in r:
            for d in r:
                if ((a and b) != c) and (b <= d) == 1:
                    print(c, a, d, b) # cadb