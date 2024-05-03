nums = list(map(int, open("files/17-282.txt").readlines()))

elem = min([n for n in nums if n % 37 == 0])

pairs = []

def check(n: int): return sum([int(x) for x in str(n)]) == sum([int(x) for x in str(elem)])
    

for i in range(len(nums) - 1):
    if check(nums[i]) or check(nums[i + 1]):
        pairs.append((nums[i], nums[i + 1]))

m = min([sum(pair) for pair in pairs])

print(len(pairs), m)
# 442 2423