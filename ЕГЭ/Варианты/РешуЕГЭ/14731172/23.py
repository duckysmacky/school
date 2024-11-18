

def fun(start, end):    
    if start > end or start == 29:
        return 0
    if start < end:
        return (fun(start + 1, end) + fun(start * 2, end) + fun(start * 3, end))
    if start == end:
        return 1

print(fun(13, 44))
# 2 3 4 5 6 12 13
# 2 3 4 5 10 11 12 13
# 2 3 4 8 9 10 11 12 13
# 2 3 4 12 13
# 2 3 9 10 11 12 13
# 2 3 6 12 13
# 2 3 6 7 8 9 10 11 12 13
# 2 6 12 13
# 2 4 12 13
# 2 4 8 9 10 11 12 13
# 2 3 4 5 6 7 8 9 10 11 12 13