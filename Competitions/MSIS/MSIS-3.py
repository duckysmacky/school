
def findIndex(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


def countCorridors(hs):
    return [len(corridors) for corridors in hs.values()]


houses = []
for dataInput in range(int(input())):
    house = {}
    totalInput = input().split()
    totalRooms = int(totalInput[0])  # rooms N
    totalCorridors = int(totalInput[1])  # corridors M
    # Creating rooms and corridors from input
    for c in range(totalCorridors):
        idInput = input().split()
        roomID = int(idInput[0])
        corridorID = int(idInput[1])
        if not house.get(roomID):
            house[roomID] = []
        house[roomID].append(corridorID)
    house = dict(sorted(house.items()))
    houses.append(house)

for house in houses:
    hours = 0

    while len(house) != 0:
        removableCorridors = []
        houseIndexes = list(house.keys())
        for indexOfMax in findIndex(countCorridors(house), max(countCorridors(house))):
            for corridor in house[houseIndexes[indexOfMax]]:
                removableCorridors.append(corridor)
            del house[houseIndexes[indexOfMax]]
        for removableCorridor in removableCorridors:
            for v in house.values():
                if removableCorridor in v:
                    v.remove(removableCorridor)
        hours += 1
    print(hours)
