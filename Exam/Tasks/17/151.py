nums = list(map(int, open("files/17-1.txt").readlines()))
# nums = [306, 36, -15, -6, 2, 16]

pairs = []

def check(n: int): return (str(n)[-1] == '6') and (n % 3 == 0)
    

for i in range(len(nums) - 1):
    if check(nums[i]) or check(nums[i + 1]):
        pairs.append((nums[i], nums[i + 1]))

m = min([min(pair) for pair in pairs])

print(len(pairs), m)
# 587 -9996