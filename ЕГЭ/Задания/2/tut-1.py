# ? ? ? ? F
# 0 1 0 0 0
# 0 1 1 0 0
# 1 1 1 0 0

# x or not y or (not z and w)
print("x y z w")
r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if (x or (not y) or ((not z) and w)) == 0:
                    print(x, y, z, w)
                    # wyzx