# ? ? ? ? F
# 0 0 ? ? 0
# 0 1 ? ? 0
# 1 1 ? 0 0

# (not (x <z)) or (y == w) or y

print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if ( (not (x <= z)) or (y == w) or y ) == 0:
                    print(x, y, z, w)
                    # xzwy