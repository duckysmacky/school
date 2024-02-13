from math import log2

# I_extra = ?

k_1 = 10
N_1 = 26 # 32
i_1 = log2(32)
I_1 = k_1 * i_1

k_2 = 5
N_2 = 10 # 16
i_2 = log2(16)
I_2 = k_2 * i_2

users = 40
I_total = 1800 * 8
I_user = I_total / users
I_extra = int((I_user - I_1 - I_2) / 8)
print(I_extra)
