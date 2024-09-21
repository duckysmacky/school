file = open("files/170.txt")
count = 0

def check(rep, uni):
    lst = []
    for r in rep:
        if rep.count(r) != 2: continue
        for u in uni:
            lst.append(r > u)
    return all(lst)

for line in file.readlines():
    data = list(map(int, line.split()))
    repeating = [x for x in data if data.count(x) != 1]
    unique = [x for x in data if data.count(x) == 1]
    if 2 <= len(repeating) == len(set(repeating)) * 2 and check(repeating, unique):
        print(data)
        count += 1
print(count) # 665