for A in range(10_000):
    valid = True
    for x in range(10_000):
        for y in range(10_000):
            if not ((x * y < A) or (x < y) or (9 < x)):
                valid = False
                break
        if not valid:
            break
    if valid:
        print(A)
        break