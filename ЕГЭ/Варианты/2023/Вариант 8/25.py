def find_sum(x: int) -> tuple | None:
    sq_sum = ()
    for a in range(1, int(x ** 0.5) + 1):
        b = (x - a ** 2) ** 0.5
        if b == int(b) and a <= b:
            if sq_sum != ():
                return None
            sq_sum = (a, int(b))
    return sq_sum

for num in range(164_361, 164_423 + 1):
    sq_sum = find_sum(num)
    if sq_sum != None and sq_sum != ():
        print(sq_sum)