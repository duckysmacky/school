from itertools import permutations

def alg(n):
    possible = [int(''.join(x)) for x in permutations(str(n), r=2) if ''.join(x)[0] != '0']
    return max(possible) - min(possible)


for n in range(100, 999 + 1):
    if alg(n) == 14:
        print(n)