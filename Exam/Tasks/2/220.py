# ? ? ? ? F
# 0 0 1 0 0
# 0 ? ? 1 0
# 1 ? 1 1 0

# ((z <= y) and ((not x) <= w)) <= ((z == w) or (y and (not x)))

print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if ( ( (z <= y) and ((not x) <= w) ) <= ( (z == w) or (y and (not x)) ) ) == 0:
                    print(x, y, z, w)
                    # yzwx