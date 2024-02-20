# ? ? ? ? F
# 0 0 0 ? 0
# 0 1 1 ? 0
# ? 1 0 1 0

# (w or x or y) <= ((y or z) and x or y and (w or z))

print("x y z w")
r = range(2)

for x in r:
    for y in r:
        for z in r:
            for w in r:
                if ( (w or x or y) <= ((y or z) and x or y and (w or z)) ) == 0:
                    print(y, w, z, x)
                    # ywzx

# 0 0 0 1
# 0 1 1 0
# 0 1 0 1

# 0 1 0 0
# 1 0 0 0
