file = open("3.txt")
order_count = int(file.readline())
orders = sorted([list(map(int, line.split())) for line in file])
couriers = []

cnt = 1
for time in orders:
    for i in range(len(couriers)):
        if couriers[i] <= time[0]:
            couriers[i] = sum(time)
            if i == 0: cnt += 1
            print("existing", time, i)
            break
    else:
        couriers.append(sum(time))
        print("new", time)
print(len(couriers), cnt)
