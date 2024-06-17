from math import log2

# N = 2 ** x
# I = k * x

N1 = 16
N2 = 2

# I1 = I2 - 21kb
# I1 = ?kb

i1 = log2(N1)  # 4
i2 = log2(N2)  # 1

# I1 = I2 - 21kb
# i1 * k = i2 * k - (21 * 8 * 1024)
# (21 * 8 * 1024) = i2k - i1k = 4k - 1k = 3k
k = (21 * 8 * 1024) / 3
I1 = k * i1  # bit
print(I1 / (8 * 1024))  # kb
# 28
