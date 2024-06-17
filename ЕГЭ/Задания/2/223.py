# ? ? ? F
# 1 ? ? 1
# 0 ? ? 1
# 1 ? 1 1

# (y <= z) and (not (z and x))

print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            if ((y <= z) and (not (z and x))) == 1:
                print(x, y, z)
                # zxy