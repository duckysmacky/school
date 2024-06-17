from math import log2

k2 = 640 * 256
I2 = 170 * 1024 * 8
#I2 - 100%
I1 = I2 + (I2 * 0.35)
# Nmax = ?

# I2 + (I2 * 0.35) = I1
# k2 * x + (k2 * x * 0.35) = k1 * x
# k1 = (k2 * x + (k2 * x * 0.35)) / x
# k1 = (ik2 + 0.35ik2) / x
k1 = k2 + 0.35 * k2
# I1 = k1 * x
i = int(I1 / k1) # 8
Nmax = 2 ** i
print(Nmax)
# 256
