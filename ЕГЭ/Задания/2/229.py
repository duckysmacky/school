# ? ? ? ? F
# 1 0 0 1 0
# 1 1 0 1 0
# 0 0 0 1 0

# ((x <= z) <= y) or (not w)

print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if ( ((x <= z) <= y) or (not w) ) == 0:
                    print(x, y, z, w)
                    # zxyw