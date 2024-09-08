for x in range(1, 2030 + 1):
    val = 7 ** 170 + 7 ** 100 - x
    num = ""
    while val > 0:
        num += str(val % 7)
        val //= 7
    if num.count('0') == 71:
        print(x)
