from math import ceil, log2

k = 13
N = 18 + 10
i = ceil(log2(N))
I = ceil(k * i / 8)
I_ex = 30 * 1024
I_n = (I + I_ex) * 30
print(I_n)