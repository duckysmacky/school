nums = list(map(int, open("files/17-345.txt").readlines()))
# file not found (17-354.txt)

elem = max(nums)

pairs = []

def check(p): return (str(max(p))[-1] == '2') and (sum([n ** 2 for n in p]) < elem ** 2)

for i in range(len(nums) - 1):
    p = (nums[i], nums[i + 1])
    if check(p):
        pairs.append(p)

m = max([sum(pair) for pair in pairs])

print(len(pairs), m)
# 71 13776