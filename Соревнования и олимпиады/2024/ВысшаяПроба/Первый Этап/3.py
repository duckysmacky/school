from math import ceil, log2

I_cube = 192 * 2 ** 50 * 8
fermones = 4096
sides = 6
I_side = I_cube / sides
i = ceil(log2(fermones))
k = I_cube / fermones
print(k)