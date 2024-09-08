r = range(2)
print("w x y z")
for w in r:
    for x in r:
        for y in r:
            for z in r:
                if ((not (not w or y) or x) or not z) == 0:
                    print(z, y, w, x)
# w x y z
# 1 0 1 1
# 0 0 0 1
# 0 0 1 1
