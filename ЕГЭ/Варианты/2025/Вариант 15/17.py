file = open("17.txt")
nums = list(map(int, file.readlines()))
triples = []

sum_all = sum(x for x in nums if x % 12 == 0)

def check(nums):
    vals = (nums[0] % (nums[1] + nums[2]) == 0) \
        + (nums[1] % (nums[2] + nums[0]) == 0) \
        + (nums[2] % (nums[0] + nums[1]) == 0)
    return vals == 1

for i in range(len(nums) - 2):
    triple = nums[i:i + 3]
    print(triple)
    if check(nums) and sum(triple) < sum_all:
        triples.append(triple)

print(len(triples), sum(max(triples, key=sum)))
