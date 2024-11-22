r = range(2)
for x in r:
    for y in r:
        for z in r:
            if ((not x or z) and (not x or not y or not z)) == 0:
                print(y, x, z)