val = 256 ** 500 * 4 ** 100 - 64 ** 30 - 8
num = ''
while val > 0:
    num += str(val % 4)
    val //= 4
print(num.count('3'))