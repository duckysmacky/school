# TODO
# ? ? ? ? F
# 0 0 0 1 0
# 1 1 0 1 0
# 0 1 ? ? 0

# ((w <= y) and ((not x) <= z)) <= ((z == w) or (y and (not x)))

print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if ( ((w <= y) and ((not x) <= z)) <= ((z == w) or (y and (not x))) ) == 0:
                    print(x, y, z, w)
                    # yxwz