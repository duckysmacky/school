def travel(start, finish, found):
    if start >= finish: return start == finish and found == 1
    if start == 16: found = 1
    return travel(start - 2, finish, found) + travel(start // 2, finish, found)

print(travel(38, 2, 0))
    