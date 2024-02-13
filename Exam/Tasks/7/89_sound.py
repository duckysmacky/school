from math import log2

x = 2
f = 48000
t = (4 * 60) + 5
I = 46 * 1024 * 1024 * 8
# imax = ?

# I = f * i * x * t
imax = int(I / (f * x * t))
print(imax)
# 16
