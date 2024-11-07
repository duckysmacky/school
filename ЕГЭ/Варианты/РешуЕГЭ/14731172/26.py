with open("14731172/26.txt") as f:
    lines = f.readlines()
    N = int(lines[0].split()[0])
    budget = int(lines[0].split()[1])
    lines.pop(0)

lines = [line.split() for line in lines]
list_A = [list(map(int, [line[1], line[0]])) for line in lines if line[2] == "A"]
# list_A.sort(reverse = True)
list_B = [list(map(int, [line[1], line[0]])) for line in lines if line[2] == "B"]
# list_B.sort(reverse = True)

lists = [list_B, list_A]
for l in lists:
    counter = 0
    for item in l:
        i = 0
        while budget >= item[1] and i < item[0]:
            budget -= item[1]
            counter += 1
            i += 1
        if i < item[0]:
            break
            
    print(f"List: {l} | Bough Items: {counter} | Left over: {budget} ")