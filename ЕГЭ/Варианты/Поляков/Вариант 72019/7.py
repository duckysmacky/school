from math import ceil, log2

k = 4044 * 1028
N_t = 256
i_t = ceil(log2(N_t))
I_res = 12 * 1024 * 1024 * 8
for N in range(1, 100_000):
    i_c = ceil(log2(N))
    i = i_c + i_t
    I = k * i
    if I <= I_res:
        print(N)