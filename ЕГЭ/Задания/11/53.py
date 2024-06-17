# TODO
from math import log2

password_len = 20
password_sym = 8
# А, В, C, D, Е, F, G, H

users = 20
I_users = 400
I_user = I_users / users
# I_extra = ?

# N = 8
i_sym = log2(8)
I_password = password_len * i_sym
# print(I_password) # 60

# N_coded = 60 => 64
I_password_coded = log2(64)

I_extra = I_user - I_password_coded
print(I_extra)
# 14
