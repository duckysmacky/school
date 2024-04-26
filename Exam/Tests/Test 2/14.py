for x in range(1, 10_000):
    s = bin(4 ** 2015 + 2 ** x - 2 ** 2015 + 15)[2:]
    if s.count("1") == 500:
        # print(s)
        break
    
print(x)
# 2510