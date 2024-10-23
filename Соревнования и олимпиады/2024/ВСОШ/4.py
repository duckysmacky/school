def right_binary_search(left: int, right: int, check_callback, args: object) -> int:
    while left < right:
        middle = (left + right + 1) // 2
        result = check_callback(middle, args)
        if result == 1:
            left = middle
        elif result == -1:
            left = middle - 1
            right -= 1
        else:
            right = middle - 1
    return left


def check(chunk_size: int, args: object) -> int:
    y, x, target_parts = args
    if chunk_size % 2 != 0 and chunk_size > max(y, x): return -1

    size = (y * x) - chunk_size
    parts = [size]

    i = -1
    while len(parts) < target_parts - 1:
        # if i < -len(parts) or parts[i] == 0: return False
        if parts[i] == 0: return False

        # if parts[i] == 1:
        #     i -= 1
        #     continue

        if parts[i] % 2 == 0:
            div = parts[i] // 2
            parts[i] = div
            parts.append(div)
        else:
            div = parts[i] // 2
            parts[i] = div + 1
            parts.append(div)
        # i = -1

    return len(parts) == target_parts - 1


def solve(y: int, x: int, target_parts: int) -> int:
    return right_binary_search(1, y * x, check, (y, x, target_parts))


m = int(input())
n = int(input())
k = int(input())

print(solve(m, n, k))