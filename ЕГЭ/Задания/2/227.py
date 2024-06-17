# ? ? ? ? F
# 1 0 1 0 0
# 0 0 1 1 0
# 0 1 1 1 0
# 1 0 1 1 0

# (a <= b) and (c <= d) or (not c)

print("a b c d")
r = range(2)
for a in r:
    for b in r:
        for c in r:
            for d in r:
                if ( (a <= b) and (c <= d) or (not c) ) == 0:
                    print(a, b, c, d)
                    # bdca