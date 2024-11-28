r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                f = (x == w) or (y and not z) or w
                if f == 0:
                    print(x, w, z, y)
