file = open("2.txt")
candidates, spots = map(int, file.readline().split())
data = []
for line in file:
    id, *points, interview = list(map(int, line.split()))
    data.append((sum(points), interview, -id))

data.sort(reverse=True)
half_passing = [d for d in data if d[0] == data[spots - 1][0]]
passing = [d for d in data[:spots - 1] if d[0] != half_passing[0][0]]
print(passing)
print(-passing[-1][2], len(half_passing))