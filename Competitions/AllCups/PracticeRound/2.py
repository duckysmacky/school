s = input().removesuffix(" ")
t = input().removeprefix(s).removesuffix(" ")

i = len(s)
x = s + ""
counter = 1
while x == s:
    s = s[:i]
    i -= 1
    counter += 1
    
print(counter)