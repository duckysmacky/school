file = open("files/9-170.csv")
count = 0


def check(rep, uni) -> bool:
    lst = []
    for r in rep:
        if rep.count(r) != 2: continue
        for u in uni:
            lst.append(r > u)
    return all(lst)


for line in file:
    nums = list(map(int, line.split(';')))
    repeating = [x for x in nums if nums.count(x) != 1]
    unique = [x for x in nums if nums.count(x) == 1]
    if len(unique) % 2 == 0 and len(unique) != 6 and check(repeating, unique):
        print(repeating, unique)
        # print(nums)
        count += 1
print(count)
