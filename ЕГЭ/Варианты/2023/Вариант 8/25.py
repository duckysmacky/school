def sq_sum(x: int) -> tuple | None:
    ab = ()
    for div in range(1, int(x ** 0.5) + 1):
        a, b = div, x // div
        if a ** 2 + b ** 2 == x:
            if ab != ():
                return None
            ab = (a, b)
    return ab

for num in range(164_361, 164_423 + 1):
    sqs = sq_sum(num)
    if sqs != None and sqs != ():
        print(sqs)