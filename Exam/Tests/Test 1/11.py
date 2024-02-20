from math import log2

k = 10
N = 52  # 64
i = log2(64)

# I_users = ?kb
users = 65_536

I_user = k * i
I_users = (I_user * users) / 1024 * 8
print(I_users)
# 30720
