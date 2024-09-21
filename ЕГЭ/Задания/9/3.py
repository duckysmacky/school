file = open("files/170.txt")
count = 0
for line in file:
    data = list(map(int, line.split()))
    repeating = [x for x in data if data.count(x) != 1]
    unique = [x for x in data if data.count(x) == 1]
    if len(unique) == 4 and min(unique) + max(unique) <= sum(repeating):
        print(data)
        count += 1
print(count) # 1159