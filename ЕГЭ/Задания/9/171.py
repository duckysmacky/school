from functools import reduce

file = open("files/9-170.csv")
count = 0
for line in file:
    nums = list(map(int, line.split(';')))
    repeating = [x for x in nums if nums.count(x) != 1]
    unique = [x for x in nums if nums.count(x) == 1]
    if len(unique) == 3 and 3 * sum(unique) <= reduce(lambda val, x: val * x, repeating):
        print(nums)
        count += 1
print(count)
