file = open("files/9.txt")
count = 0
for line in file:
    nums = list(map(int, line.split()))
    repeating = [x for x in nums if nums.count(x) != 1]
    unique = [x for x in nums if nums.count(x) == 1]
    if len(unique) == 3 and sum(repeating) ** 2 > sum(unique) ** 2:
        count += 1
print(count)
