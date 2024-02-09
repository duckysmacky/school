# ? ? ? F
# ? 1 ? 0
# 1 1 ? 0

# (x == y) or (x <= (z and y))

print("x y z")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            if ((x == y) or (x <= (z and y))) == 0:
                print(x, y, z)
                # zxy