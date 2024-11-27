from math import ceil, log2

k = 31
N = 13
i = ceil(log2(N))
I_base = ceil(i * k / 8)
I_n = 20 * 1024
n = 337
I_alloc = I_n / n

for I_extra in range(1, 10_000):
    I = I_base + I_extra
    if I < I_alloc:
        print(I_extra)