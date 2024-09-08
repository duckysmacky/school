from math import ceil

N = 10 + 52 + 963 # 1025 -> 2048
i = 11
n_numbers = 2000
I_numbers = 693 # Kb
# k = ?

max_k = 0
for k in range(1, 1000):
    I_number = ceil((k * i) / 8)
    _I_numbers = (n_numbers * I_number) / 1024
    if _I_numbers <= I_numbers:
        max_k = max(max_k, k)
print(max_k)
