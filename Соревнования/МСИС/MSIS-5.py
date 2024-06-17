def doMult(nums, k):
    for i in range(len(nums)):
        if not nums[i] ** k > 10 ** 5:
            nums[i] = nums[i] ** k

    print(nums)


def doRoot(nums, k):
    for i in range(len(nums)):
        if nums[i] ** (1 / k).is_integer():
            nums[i] = nums[i] ** (1 / k)

    print(nums)


def doSum(nums, l, r):
    print(sum(nums[l:r + 1]))


for n in range(int(input())):
    nums = list(map(int, input().split()))
for q in range(int(input())):
    inp = input().split()
    t = int(inp[0])
    if t == 1:
        doMult(nums, int(inp[1]))
        print("mult")
    elif t == 2:
        doRoot(nums, int(inp[1]))
        print("root")
    elif t == 2:
        doSum(nums, int(inp[1]), int(inp[2]))
        print("sum")
