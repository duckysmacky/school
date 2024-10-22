def f(n):
    if n <= 1: return 1
    if n == 2: return 2
    if n > 2 and n % 3 == 0: 2 * n - f(n // 3) - f(n - 1)