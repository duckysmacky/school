def find(start: int, end: int) -> int:
    if start > end: return 0
    if start == end: return 1
    return find(start + 1, end) + find(start + 7, end)

print(find(5, 12) * find(12, 26))