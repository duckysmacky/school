x = 125 + 25**3 + 5**9
count = 0
while x > 0:
    if x % 5 == 0:
        count += 1
    x = x // 5
print(count)