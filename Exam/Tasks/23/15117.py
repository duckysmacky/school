from itertools import product, permutations

one = lambda x: x + 1
two = lambda x: x + 2

pr = list(permutations((one, two), 20 - 3))

def F(x, target):
    v = False
    i = 0
    while x != target:
        if x == 15: return False
        if x == 9: v = True
        x = pr[i](x)
        i += 1
    return v and True
    
c = 0
if F(3, 20):
    c += 1