r = range(1221, 9764)

nums = []

for n in r:
    if (n % 7 == 0) and (n % 2 != 0 and n % 5 != 0 and n % 11 != 0 and n % 49 != 0):
        nums.append(n)
        
print(len(nums), max(nums))
# 380 9737