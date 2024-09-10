from functools import reduce

file = open("files/9-162.txt")
count = 0
for line in file:
    nums = sorted(list(map(int, line.split())), reverse=True)
    biggest, *others = nums
    if (biggest ** 3 >= 2 * reduce(lambda val, x: val * x, others)
            and all([x > 10 for x in nums])):
        count += 1
print(count)
