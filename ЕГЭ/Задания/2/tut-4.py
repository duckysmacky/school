# ? ? ? ? F
# 0 0 0 ? 1
# 0 0 ? 1 1
# 0 ? ? 1 1

# ((y <= z) <= (x and y)) and (x <= w)

print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if (((y <= z) <= (x and y)) and (x <= w)) == 1:
                    print(x, y, z, w)
                    # zxwy