from math import log2, ceil
# N = 2^i | I = k * i
k1 = 1024 * 768
I1 = 2 * 1024 * 1024 * 8
print(k1, I1)


k2 = 100 ** 2
N2 = 64
i2 = log2(64)
I2 = 96 * 1024 * 8

i1 = ceil(I1 / k1)
print(i1)
N1 = 2 ** i1
print(N1) # 4194304