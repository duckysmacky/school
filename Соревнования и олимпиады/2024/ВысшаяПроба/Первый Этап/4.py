L, R = map(int, input().split())
# TODO: optimize
cnt = 0
for size in range(L, R + 1):
    if size % 3 == 0:
        cnt += 1
print(cnt)