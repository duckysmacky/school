file = open("26_10072.txt")
# file = open("test")
n = int(file.readline())
nums = list(map(int, file.readlines()))

triples = []
for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            tr = (nums[i], nums[j], nums[k])
            triples.append(tr)
print(len(triples), sum(max(triples, key=sum)))
