from math import log2

password_len = 15
password_symbols = 8
# А, В, C, D, Е, F, G, H

users = 20
I_users = 320
I_user = I_users / users
# I_extra = ?

# N = 8
i_symbols = log2(8)
I_password = password_len * i_symbols
# print(I_password) # 45

# N_coded = 45 => 64
I_password_coded = log2(64)

I_extra = I_user - I_password_coded
print(I_extra)
# 10
