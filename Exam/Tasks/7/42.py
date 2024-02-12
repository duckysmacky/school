from math import log2

k = 800 * 600
# I <= 100kb
# Nmax?

# I = k * i
# i = I / k
i = int((100 * 8 * 1024) / k)  # bit
N = 2 ** i
print(N)
# 2
