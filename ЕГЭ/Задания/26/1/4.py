file = open("4-test.txt")
gnomes = int(file.readline())
data = list(map(int, file.readlines()))
pots = [0, 0, 0]

for time in data:
    best_pot = -1
    for i in range(len(pots) - 1):
        pot1 = pots[i]
        pot2 = pots[i + 1]
        
