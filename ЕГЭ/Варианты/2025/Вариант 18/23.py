def f(s, e):
    if s > e: return 0
    if s == 11 or s == 17: return 0
    if s == e: return 1
    return f(s + 1, e) + f(s + 4, e) + f(s * 2, e)

print(f(3, 24))
