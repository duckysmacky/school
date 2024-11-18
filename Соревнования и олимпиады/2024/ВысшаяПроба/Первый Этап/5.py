def get(x: int) -> bool:
    if x < 4: return False
    divs = [1, x]
    for div in range(2, x):
        if (rem:= x % div) == 0:
            divs.append(div)
        if len(divs) > 3:
            return False
    return len(divs) == len(set(divs)) == 3

amount = [x for x in range(4000 + 1) if get(x)]
day = int(input()) - 1
print(amount[day])