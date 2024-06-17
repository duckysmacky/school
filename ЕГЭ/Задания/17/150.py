nums = list(map(int, open("files/17-1.txt").readlines()))
# nums = [-45, 14, 22, -21, 34]

pairs = []

def check(n1: int, n2: int): return (n1 % 7 == 0) and (n2 % 17 != 0)
    

for i in range(len(nums) - 1):
    if check(nums[i], nums[i + 1]) or check(nums[i + 1], nums[i]):
        pairs.append((nums[i], nums[i + 1]))

minsum = min([sum(pair) for pair in pairs])        

print(len(pairs), minsum)
# 2510 -19677