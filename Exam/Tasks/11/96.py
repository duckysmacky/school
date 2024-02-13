from math import log2

k_1 = 15
N_1 = 26 # 32
i_1 = log2(32)
I_1 = k_1 * i_1

k_2 = 4
N_2 = 6 # 8
i_2 = log2(8)
I_2 = k_2 * i_2

I_alloc = 1600
I_extra = 12

I_user = int(I_1 + I_2 + I_extra)
users = I_alloc / I_user
print(int(users))
# 17
