args1 = input().split()
n = int(args1[0])
k = int(args1[1])

args2 = input().split()
for i in range(len(args2)):
    k -= int(args2[i])


print(k)