file = open("Задание 9/9.csv")
file.readline()

min_p = 10 ** 10
avg_p = 0
cnt = 0
for line in file:
    date, *pressure = line.split(';')
    pressure = list(map(lambda x: float(x.replace(',', '.')), pressure)) 
    min_p = min(min_p, min(pressure))
    avg_p += sum(pressure)
    cnt += len(pressure)
avg_p /= cnt
print(avg_p - min_p)