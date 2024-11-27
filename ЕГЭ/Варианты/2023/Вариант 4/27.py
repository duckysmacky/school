from itertools import product

file = open("27-b.txt")
pairs, max_skips = map(int, file.readline().split())
nums = [list(map(int, line.split())) for line in file.readlines()]
nums.append([0, 0])

def get_moveset(max_skips: int, skips: int) -> list:
    moveset = list(product((0, 1), repeat=2))
    if max_skips - skips == 1 and (0, 0) in moveset:
        moveset.remove((0, 0))
    return moveset

result_sum = 0
skips = 0
for i in range(len(nums) - 1):
    if skips == max_skips:
        result_sum += nums[i][1]
        skips = 0
        continue
    
    this, next = nums[i], nums[i + 1]
    moveset = get_moveset(max_skips, skips)
    best_result = -100_000
    best_moves = ()
    for moves in moveset:
        result = this[moves[0]] + next[moves[1]]
        if result > best_result:
            best_result = result
            best_moves = moves

    if best_moves[0] == 0:
        skips += 1
    result_sum += this[best_moves[0]]
print(result_sum)    