file = open("26.txt")
N = int(file.readline())
freezer_cnt = int(file.readline())
freezer_size = int(file.readline())
weights = sorted(list(map(int, file.readlines())), reverse=True)

freezer_idx = 0
while len(weights) > 0:
    freezer_idx += 1
    size = freezer_size
    while size != 0 and len(weights) > 0:
        for i in range(len(weights)):
            if size - weights[i] >= 0:
                size -= weights[i]
                weights.pop(i)
                break
        else:
            if i == len(weights) - 1:
                break
    
print(freezer_idx, size)