from math import log2

k1 = 400 ** 2
I1 = 2 * 1024 * 1024 * 8

k2 = 100 ** 2
N2 = 64
i2 = log2(64)
I2 = 96 * 1024 * 8

# N1 = ?

# p = I2 / I1 = (k2 * i2) / (k1 * i1)
p = I2 / I1

# (p * k1 * i1) = (k2 * i2)
# i1 = k2 * i2 / p * k1
i1 = int((k2 * i2) / (p * k1))
N1 = 2 ** i1

print(N1)
# 256