from itertools import product

file = open("27-a.txt")
pairs, max_skips = map(int, file.readline().split())
nums = [list(map(int, line.split())) for line in file.readlines()]

moveset = product(('0', '1', '2'), repeat=pairs)

best_result = 0
for moves in moveset:
    moves = ''.join(moves)
    if '0' * (max_skips + 1) in moves.replace('2', ''):
        continue
    result = 0
    for i in range(pairs):
        move = int(moves[i])
        result += nums[i][move] if move != 2 else 0
    if result > best_result:
        best_result = result
print(best_result)