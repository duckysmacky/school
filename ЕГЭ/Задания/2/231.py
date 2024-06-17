# ? ? ? ? F
# 0 1 0 1 1
# 0 1 1 1 1
# 1 0 1 1 1

# ((not x) <= y) and ((not y) == z) and w

print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if ( ((not x) <= y) and ((not y) == z) and w ) == 1:
                    print(x, y, z, w)
                    # zyxw