def left_binary_search(left: int, right: int, check_callback, args: object) -> int:
    while left < right:
        middle = (left + right) // 2
        if check_callback(middle, args):
            right = middle
        else:
            left = middle + 1
    return left


def check(stone_weight: int, args: object) -> bool:
    weights, difference = args
    return sum(weights[:2]) - (weights[2] + stone_weight) <= difference


def solve(weights: list, difference: int) -> int:
    return left_binary_search(0, sum(weights), check, (sorted(weights), difference))


# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())

assert solve([30, 40, 35], 10) == 15
assert solve([30, 20, 45], 10) == 0

# print(solve([A, B, C], D))