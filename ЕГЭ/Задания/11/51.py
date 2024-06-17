from math import log2

password_len = 11
symbols = 12
# [A, B, C, D, E, F, G, H, K, L, M, N]

Users = 50
I_users = 700
# I_extra = ?
I_user = I_users / 50

# N = 12 => 16
i_symbols = log2(16)
I_password = password_len * i_symbols  # 44
# N = 44 => 64
I_password_coded = log2(64)

I_extra = I_user - I_password_coded
print(I_extra)
# 8
