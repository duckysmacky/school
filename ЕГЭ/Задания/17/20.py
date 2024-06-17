r = range(1045, 8964)

nums = []

for n in r:
    if (n % 5 == 0 or n % 7 == 0) and (n % 11 != 0 and n % 13 != 0 and n % 17 != 0 and n % 19 != 0):
        nums.append(n)
        
print(len(nums), min(nums))
# 1867 1050