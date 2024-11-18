from string import digits, ascii_uppercase
from fnmatch import fnmatch

alph = digits + ascii_uppercase

def conv(x: int, p: int) -> str:
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

for n in range(1, 223):
    n16 = conv(n, 16)
    n8 = conv(n, 8)
    n4 = conv(n, 4)
    n2 = conv(n, 2)
    print(n16, n8, n4, n2)

print(int("DB", 16))