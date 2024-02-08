with open("14731172/17.txt") as f:
    lines = f.readlines()

thirds = []
for i in range(0, len(lines) - 2, 3):
    thirds.append([lines[i].strip(), lines[i + 1].strip(), lines[i + 2].strip()])

print(lines[0:9])
print(thirds[0:3])

count = 0
max_sum = 0
for set in thirds:
    max_num = max(map(int, set))
    set.pop(set.index(str(max_num)))
    if max_num**2 < (int(set[0])**2 + int(set[1])**2):
        count += 1
        max_sum = max(max_sum, max_num + sum(map(int, set)))

print(count)
print(max_sum)
