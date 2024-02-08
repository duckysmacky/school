import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def checkHexagon(coords):
    sides = []
    diagonals = []
    distances = []

    for i in range(6):
        x1, y1 = coords[i]
        x2, y2 = coords[(i+1)%6]
        sides.append(distance(x1, y1, x2, y2))

    for i in range(3):
        x1, y1 = coords[i]
        x2, y2 = coords[(i+3)%6]
        diagonals.append(distance(x1, y1, x2, y2))

    for i in range(6):
        x1, y1 = coords[i]
        x2, y2 = coords[(i+3)%6]
        distances.append(distance(x1, y1, x2, y2))

    side_min = min(sides)
    side_max = max(sides)
    diag_min = min(diagonals)
    diag_max = max(diagonals)
    dist_min = min(distances)
    dist_max = max(distances)

    if side_max / side_min <= 111 / 100 and diag_max / diag_min <= 111 / 100 and dist_max / dist_min <= 111 / 100:
        return '1'
    else:
        return '0'

t = int(input())
result = ''

for _ in range(t):
    coords = []
    for _ in range(6):
        x, y = map(int, input().split())
        coords.append((x, y))
    result += checkHexagon(coords)

print(result)