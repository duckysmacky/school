file = open("26_9847.txt")
n = int(file.readline())

changes = [0] * (24 * 60)
for line in file:
    start, end = map(int, line.split())
    changes[start] += 1
    changes[end] -= 1

cnt = 0
visitors = [0] * (24 * 60)
for i in range(len(changes)):
    cnt += changes[i]
    visitors[i] = cnt

peaks = 0
for i in range(len(visitors) - 1):
    if visitors[i] != visitors[i + 1] and visitors[i] == max(visitors):
        peaks += 1

print(peaks, max(visitors))
