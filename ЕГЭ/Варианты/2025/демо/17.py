file = open("files/demo_2025_17.txt")
data = list(map(int, file.readlines()))
min_num = min(data)
pairs = []


def check(a: int, b: int) -> bool:
    return a % 16 == min_num or b % 16 == min_num


for i in range(len(data) - 1):
    pair = (data[i], data[i + 1])
    if check(*pair):
        pairs.append(sum(pair))
print(len(pairs), max(pairs))
