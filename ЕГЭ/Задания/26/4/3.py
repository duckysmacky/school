file = open("26_9077.txt")
p_cnt, n = map(int, file.readline().split())

max_time = 24 * 60 * 60

changes = [[0] * max_time for _ in range(p_cnt)]
for line in file:
    start, length, p_from, p_to = map(int, line.split())
    end = start + length - 1
    changes[p_from - 1][start] -= 1
    changes[p_to - 1][end] += 1

parkings = [[0] * max_time for _ in range(p_cnt)]
for p in range(len(changes)):
    cnt = 0
    for i in range(len(changes[p])):
        cnt += changes[p][i]
        parkings[p][i] = cnt

stock = [0] * p_cnt
for p in range(len(parkings)):
    stock[p] = -min(parkings[p])

peak = [0] * max_time
for t in range(max_time):
    cnt = 0
    for p in range(len(parkings)):
        cnt += parkings[p][t]
    peak[t] = max(peak[t], -cnt)

print(sum(stock))
print(max(peak) + 1)
