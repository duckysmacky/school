def find(start: int, end: int) -> int:
    if start > end: return 0
    if start == end: return 1
    return find(start + 1, end) + \
        (find(start + 10, end) if str(start)[-2] != '9' else find(start, end))

print(find(10, 33))