from math import log2

# I_extra = ?

k_1 = 11
N_1 = 15 + 10 # 32
i_1 = log2(N_1)
I_1 = k_1 * i_1

k_2 = 8
N_2 = (26 * 2) + 10 # 64
i_2 = log2(64)
I_2 = k_2 * i_2

I_total = 30 * 8
I_extra = int(I_total - I_1 - I_2)
print(I_extra)