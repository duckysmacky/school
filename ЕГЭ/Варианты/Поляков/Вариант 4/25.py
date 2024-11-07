from math import sqrt

def find_divs(num: int) -> list:
    divs = []
    for div in range(1, int(sqrt(num)) + 1, 2):
        if num % div == 0:
            divs.append(div)
            if div != num // div:
                divs.append(num // div)
        if len(divs) > 5:
            return []
    return divs

for num in range(105_000_000, 115_000_000 + 1):
    num_divs = find_divs(num)
    if len(num_divs) == 5:
        print(num, max(num_divs))