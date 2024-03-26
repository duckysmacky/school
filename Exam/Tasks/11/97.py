# TODO
from math import log2

I_extra = 13
I_alloc = 1800

k_1 = 15
N_1 = 26 # 32
i_1 = log2(32)
I_1 = k_1 * i_1

k_2 = 5
N_2 = 10 # 16
i_2 = log2(16)
I_2 = k_2 * i_2

I_user = I_1 + I_2 + I_extra
users = int(I_alloc / I_user)
print(users)
# 16