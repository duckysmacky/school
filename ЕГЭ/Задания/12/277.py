def f(s):
    while "555" in s or "888" in s:
        s = s.replace("555", "8", 1)
        s = s.replace("888", "55", 1)
    return s


for i in range(201, 10_000):
    S = f(i * "5")
    if S.count("5") == S.count("8"):
        print(i)
        break
# 204
