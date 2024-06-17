# ? ? ? ? F
# 1 ? ? ? 0
# 1 ? 1 ? 0
# 1 1 1 ? 0

# (x and z) or ((z <= y) <= (w <= x))

print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if ((x and z) or ((z <= y) <= (w <= x))) == 0:
                    print(x, y, z, w)
                    # wzyx