rows = int(input())
columns = int(input())
words = str(input()).split(" ")
mines = []

wordCount = 0
for y in range(rows):
    xMines = []
    for x in range(columns):
        xMines.append(words[wordCount].lower() == "true")
        wordCount += 1
    mines.append(xMines)


def checkMine(mines, y, x):
    value = 0

    for index, mine in enumerate(mines[y]):
        if mine:
            if abs(index - x) == 1:
                value += 1

    for index, mine in enumerate(mines):
        if mine[x]:
            if abs(index - y) == 1:
                value += 1
        elif x != 0:
            if mine[x - 1]:
                if abs(index - y) == 1:
                    value += 1
        elif x != len(mines[0]) - 1:
            if mine[x + 1]:
                if abs(index - y) == 1:
                    value += 1
    return value


def draw(mines, rows, columns):
    matrix = []
    for y in range(rows):
        xMatrix = []
        for x in range(columns):
            xMatrix.append(checkMine(mines, y, x))
        matrix.append(xMatrix)

    for i in matrix:
        print(' '.join(map(str, i)))


draw(mines, rows, columns)
