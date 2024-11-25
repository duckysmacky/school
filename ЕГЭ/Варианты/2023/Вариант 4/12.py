def alg(s: str) -> str:
    while "01" in s or "02" in s:
        s = s.replace("02", "1110", 1)
        s = s.replace("01", "2210", 1)
    return s

def num_sum(s: str) -> int:
    return sum(map(int, s))

s_sums = []
for length in range(69, 200):
    for twos in range(80 + 1):
        s = '0' + (length - twos) * '1' + twos * '2'
        s_sum = num_sum(s)
        res_sum = num_sum(alg(s))
        sum_root = res_sum ** 0.5
        if sum_root == int(sum_root):
            s_sums.append(s_sum)
print(min(s_sums))