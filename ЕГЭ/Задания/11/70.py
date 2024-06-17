from math import log2

pCode_k = 14
pCode_N = 26 + 10 # 36 => 64
pCode_i = log2(64)
I_pCode = int(pCode_k * pCode_i / 8)

gCode_k = 8
gCode_N = (6 * 2) + 10 # 22 => 32
gCode_i = log2(32)
I_gCode = int(gCode_k * gCode_i / 8)

I_total = 30
# I_extra = ?
I_extra = I_total - I_pCode - I_gCode
print(I_extra)
# 15
