# ? ? ? ? F
# 1 0 0 0 0
# 0 1 0 0 0
# 1 0 1 0 0

# (y or x) == (y <= w) or (not z)

print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if ( (y or x) == (y <= w) or (not z) ) == 0:
                    print(x, y, z, w)
                    # ????
# 0 0 1 0
# 0 0 1 1
# 0 1 1 0
# 1 1 1 0