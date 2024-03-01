def f(s: str):
    while "25" in s or "35" in s or "555" in s:
        while "555" in s or "11" in s or "2" in s:
            if "555" in s:
                s = s.replace("555", "1", 1)
            if "11" in s:
                s = s.replace("11", "25", 1)
            if "2" in s:
                s = s.replace("2", "5", 1)
    return s.replace(">", "")


d = {}

for n in range(101, 10_000):
    if n % 9 == 0:
        S = f(n * "5")
        d[int(S)] = n

print(d.get(max(d.keys())))
# 981
