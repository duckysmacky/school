from math import log2, ceil
# N = 2^i | I = k * i
k = 1024 * 120
I = 210 * 1024 * 8
i = 7
N = 2 ** i
i_trans = 7
for i in range(7, 30):
    if I < (k * i):
        print(i - 1) # 14
        break