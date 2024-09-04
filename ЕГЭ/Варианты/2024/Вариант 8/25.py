number_range = range(163461, 164423 + 1)
test_range = range(50, 54 + 1)
ans = []


def find_pair(x: int) -> (int, int):
    count = 0
    pair = ()

    for a in range(1, x + 1):
        b = x - a
        while a <= b:
            print(a, b)
            if a ** 2 + b ** 2 == x:
                count += 1
                pair = a, b
                if count > 1:
                    return 0, 0
            b -= 1

    if count == 1:
        return pair
    else:
        return 0, 0


for n in number_range:
    pair = find_pair(n)
    if pair != (0, 0):
        ans.append(pair)

for p in ans: print(p)
