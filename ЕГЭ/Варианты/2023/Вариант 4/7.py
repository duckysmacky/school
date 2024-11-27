from math import log2, ceil

k = 2048 * 1600
I_extra = 64 * 1024 * 8
I_n = 12 * 1024 * 1024 * 8
n = 32
I_alloc = I_n / n

for N in range(1, 100_000):
    i = ceil(log2(N))
    I_base = k * i + I_extra
    I_comp = ceil(I_base / 8)
    if I_comp <= I_alloc:
        print(N)