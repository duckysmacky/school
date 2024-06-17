nums = list(map(int, open("files/17-282.txt").readlines()))

elem = min([n for n in nums if n % 21 == 0])

pairs = []

def check(n: int): return sum(map(int, oct(n)[2:])) == sum(map(int, oct(elem)[2:]))

for i in range(len(nums) - 1):
    if check(nums[i]) or check(nums[i + 1]):
        pairs.append((nums[i], nums[i + 1]))

m = min([sum(pair) for pair in pairs])

print(len(pairs), m)
# 1703 2281