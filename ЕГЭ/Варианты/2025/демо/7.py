from math import log2

# I = k * i
# N = 2 ** i
# S = v * t

k = 1024 * 768
N = 4096
v_transfer = 1_310_720 # bit / sec
t_transfer = 300 # seconds

i = log2(N) # 12
V_packet = v_transfer * t_transfer # 393216000 bit
I_packet = k * i # 9437184 bit
n_packet = V_packet / I_packet
print(n_packet)
