def find(start: int, end: int, history: str) -> int:
    if start > end: return 0
    if start == end and history[-2] == '1': return 1
    return find(start + 1, end, history + '1') + find(start * 2, end, history + '2')

print(find(4, 24, ""))