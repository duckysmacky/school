from math import log2, ceil
# N = 2^i | I = k * i
N = 256
i = log2(256)
k = 512 * 192
t = 10
day_in_sec = 24 * 60 * 60
photos = day_in_sec / t

I = ceil((k * i * photos) / (1024 * 1024 * 8))
print(I) # 810