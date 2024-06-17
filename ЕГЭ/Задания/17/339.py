nums = list(map(int, open("files/17-339.txt").readlines()))

elem = min([n for n in nums if (n % 19 == 0 and n > 0)])

pairs = []

def check(pair): return sum(pair) < elem

for i in range(len(nums) - 1):
    p = (nums[i], nums[i + 1])
    if check(p):
        pairs.append(p)

m = abs(max([sum(pair) for pair in pairs]))

print(len(pairs), m)
# 4984 696