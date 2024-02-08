x = range(35000000, 40000001)

numbers = []
for num in x:
    num_divs = []
    for dividor in x:
        if dividor == num:
            continue
        if num % dividor == 0 and not(dividor in num_divs):
            num_divs.append(dividor)
    print(f"Number: {num} | Dividors: {num_divs}")
    if len(num_divs) == 5 and list(all(map(lambda x: x % 2 != 0, num_divs))):
        numbers.append(num)
        
print(numbers)