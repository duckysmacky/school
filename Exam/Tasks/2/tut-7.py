# ? ? ? ? F | ? ? ? ? F
# ? 0 0 ? 1 | 1 0 0 ? 1
# 0 0 ? 0 1 | 0 0 1 0 1
# 1 1 1 ? 0 | 1 1 1 0 0
#         !

# ((w <= x) == (z <= y)) and ((not y) or w)

print("x y z w F")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                f = int(((w <= x) == (z <= y)) and ((not y) or w))
                print(x, y, z, w, f)
                # zyxw

# 0 0 1 1 1
# 1 0 0 0 1
# 1 1 1 0 0
