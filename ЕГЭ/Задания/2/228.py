# ? ? ? ? F
# 1 1 0 1 0
# 0 1 0 1 0
# 0 0 0 1 0

# (not (w <= z)) or (x <= y) or (not x)

print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if ( (not (w <= z)) or (x <= y) or (not x) ) == 0:
                    print(x, y, z, w)
                    # wzyx