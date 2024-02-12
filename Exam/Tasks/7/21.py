from math import log2

# N = 2 ** i
# I = k * i

N1 = 256
N2 = 2
# I2 = I1 - 7 (kb)

i1 = log2(N1)  # 8
i2 = log2(N2)  # 1

# I2 = I1 - 7kb
# i2 * k = i1 * k - 7 * 8 * 1024
# 7 * 8 * 1024 = i1k - i2k = 8k - 1k = 7k
k = (7 * 8 * 1024) / 7
I1 = k * i1  # (bit)
print(I1 / (1024 * 8))  # kb
# 8
