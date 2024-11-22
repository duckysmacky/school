r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                f = (not ((not y or x) and (z or w))) or ((x and (not w)) or (y == z))
                if not f:
                    print(z, w, y, x)
# 1 0 0 0
# 1 1 0 1
# 0 1 1 1
# 1 0 0 1