# ? ? ? ? F
# 1 0 0 0 1
# 1 0 1 0 1
# 1 0 1 1 1
# 1 1 0 0 1

# ((a and b) == (not c)) and (b <= d)

r = range(2)
print("a b c d")
for a in r:
    for b in r:
        for c in r:
            for d in r:
                if (((a and b) == (not c)) and (b <= d)) == 1:
                    print(a, b, c, d)
                    # cadb