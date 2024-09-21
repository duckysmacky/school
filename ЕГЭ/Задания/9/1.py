from functools import reduce

file = open("files/170.txt")
count = 0
for line in file.readlines():
    data = list(map(int, line.split()))
    repeating = [x for x in data if data.count(x) != 1]
    unique = [x for x in data if data.count(x) == 1]
    if len(unique) == 3 and len(set(repeating)) == 1 and 3 * sum(unique) <= reduce(lambda val, x: val * x, repeating):
        print(data)
        count += 1
print(count) # 134