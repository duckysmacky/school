from math import log2

x = 2
f = 64000
i = 16
I = 48 * 1024 * 1024 * 8
# t = ? (min)

# I = f * x * x * t
t = I / (f * i * x)
t_min = int(t) / 60
print(t_min)
# 3