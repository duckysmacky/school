r = range(2)
for w in r:
    for x in r:
        for y in r:
            for z in r:
                if ((not x or w) and (not y or z) or w) == 0:
                    print(w, x, z, y)
# 0 1 0 0
# 0 1 1 0
# 0 0 0 1
# 0 1 0 1
# 0 1 1 1

print(1 * 3 * 1 * 1)
# 1 - wzyx
# 2 - wyzx
# 3 - wzxy