N_friends = int(input())
called = set(map(int, input().split()))
nums = set(n for n in range(1, max(called) + 3))
not_called = nums - called

print(sorted(not_called)[1])