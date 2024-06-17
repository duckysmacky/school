from math import log2

N = 256
i = log2(256) # 7
k = 512 * 192
t = 10
day_in_sec = 60 * 60 * 24
photos = day_in_sec / t

I = int((k * i * photos) / (1024 * 1024 * 8))
print(I)
# 810