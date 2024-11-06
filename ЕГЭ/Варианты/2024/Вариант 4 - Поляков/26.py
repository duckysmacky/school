file = open("26.txt")
N_total = int(file.readline())
data = []
for line in file:
    start, end = map(int, line.split())
    data.append([start, end, end - start])
data.sort()

end_time = 0
conf_cnt = 0
while len(data) > 0:
    confs = [data.pop()]
    for conf in data[::-1]:
        if conf[1] <= confs[-1][0]:
            confs.append(conf)
    end_time = max(end_time, confs[0][1])
    conf_cnt = max(conf_cnt, len(confs))

print(conf_cnt, end_time)