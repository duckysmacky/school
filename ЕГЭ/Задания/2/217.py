# TODO
# ? ? ? ? F
# 1 ? ? ? 1
# 1 1 ? ? 1
# ? 1 1 ? 1

# ((not a) <= b) and (b == (not c)) and (not d)

print("a b c d")
r = range(2)
for a in r:
    for b in r:
        for c in r:
            for d in r:
                if (((not a) <= b) and (b == (not c)) and (not d)) == 1:
                    print(a, b, c, d)
                    # cabd