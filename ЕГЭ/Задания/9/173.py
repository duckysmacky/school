from functools import reduce
from statistics import geometric_mean

file = open("files/9-170.csv")
count = 0
for line in file:
    nums = list(map(int, line.split(';')))
    repeating = [x for x in nums if nums.count(x) != 1]
    unique = [x for x in nums if nums.count(x) == 1]
    if len(unique) == 2 and geometric_mean(repeating) >= reduce(lambda val, x: val * x, unique):
        print(repeating, unique)
        count += 1
print(count)
