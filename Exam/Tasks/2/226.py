# ? ? ? F
# ? ? ? 1
# 1 ? 1 1
# 1 ? 0 1

# (not (z or x)) or y and (not x) and (z and y <= z)

print("x y z")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            if ( (not (z or x)) or y and (not x) and (z and y <= z) ) == 1:
                print(x, y, z)
                # yxz