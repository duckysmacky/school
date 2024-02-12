from math import log2

i1 = 24
N1 = 2 ** i1
I1avg = 15  # mb

N2 = 256
i2 = log2(N2)
# I2avg = ?mb

# I = k * i
k = I1avg / i1

I2avg = k * i2
print(I2avg)
# 5
