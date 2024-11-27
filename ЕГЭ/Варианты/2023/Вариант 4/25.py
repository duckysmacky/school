def find_divs(x: int) -> set | None:
    divs = set()
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            divs.add(div)
            divs.add(x // div)
        if len(divs) > 3:
            return None
    return divs if len(divs) == 3 else None

# for num in range(100_000):
#     sqrt4 = num ** 0.25
#     if sqrt4 != int(sqrt4):
#         continue
#     divs = find_divs(num)
#     if divs != None:
#         print(num, divs)

for num in range(50_034_679, 92_136_895 + 1):
    sqrt4 = num ** 0.25
    if sqrt4 != int(sqrt4):
        continue
    divs = find_divs(num)
    if divs != None:
        print(num, max(divs))