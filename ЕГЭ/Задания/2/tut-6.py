# ? ? ? ? F | ? ? ? ?
# 0 0 0 ? 1 | 0 0 0 1
# ? 1 1 1 1 | 0 1 1 1
# 1 1 0 ? 1 | 1 1 0 0

# ((x or w) == y) and (x == (not z))

print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if (((x or w) == y) and (x == (not z))) == 1:
                    print(x, y, z, w)
                    # xywz