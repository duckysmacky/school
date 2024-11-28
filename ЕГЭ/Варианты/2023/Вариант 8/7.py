from math import ceil, log2

k = 288 * 1152
N = 60
i = ceil(log2(N))
I = ceil(k * i / 8 / 1024)
print(I)