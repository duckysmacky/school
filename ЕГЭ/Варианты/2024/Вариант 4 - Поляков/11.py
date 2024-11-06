from math import ceil, log2

k1 = 10
N1 = 26
k2 = 8
N2 = 10
n = 60
I_n = 1980 # bytes
I_res = I_n / n

i1 = ceil(log2(N1))
i2 = ceil(log2(N2))
I1 = ceil(k1 * i1 / 8)
I2 = ceil(k2 * i2 / 8)
I_extra = I_res - I1 - I2
print(I_extra)