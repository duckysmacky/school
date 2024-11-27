file = open("17.txt")
nums = list(map(int, file.readlines()))
pairs = []
min_elem = min(x for x in nums if x % 103 == 0)

for i in range(len(nums) - 1):
    pair = nums[i:i + 2]
    if sum(pair) % 2 == 0 and (max(pair) - min(pair)) % min_elem == 0:
        pairs.append(pair)
print(len(pairs), sum(max(pairs, key=sum)))