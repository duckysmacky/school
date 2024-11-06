def convert(s: str) -> str:
    while "52" in s or "2222" in s or "1122" in s:
        if "52" in s:
            s = s.replace("52", "11")
        if "2222" in s:
            s = s.replace("2222", "5")
        if "1122" in s:
            s = s.replace("1122", "25")
    return s

lst = []
for n in range(4, 10_000):
    s = '5' + n * '2'
    result = convert(s)
    num_sum = sum(map(int, result))
    if num_sum == 64:
        lst.append(n)
print(max(lst))