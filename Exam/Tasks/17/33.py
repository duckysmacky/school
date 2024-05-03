r = range(1000, 10000)

nums = []

def conv(x: int, p: int) -> str:
    num = []
    while x > 0:
        num.append(x % p)
        x = x // p
    return "".join((map(str, num[::-1])))
        

for n in r:
    if (n % 5 != 0 and n % 7 != 0 and n % 11 != 0) and len(conv(n, 3)) == 8:
        nums.append(n)
        
print(min(nums), max(nums))
# 2187 6558