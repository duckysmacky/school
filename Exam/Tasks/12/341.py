def f(s: str):
    while "25" in s or "35" in s or "555" in s:
        if "25" in s:
            s = s.replace("25", "53", 1)
        if "35" in s:
            s = s.replace("35", "2", 1)
        if "555" in s:
            s = s.replace("555", "23", 1)
    return s


for n in range(3, 10_000):
    S = "2" + n * "5"
    if sum(list(map(int, f(S)))) & 7 == 0:
        print(n)
        break
# 9
