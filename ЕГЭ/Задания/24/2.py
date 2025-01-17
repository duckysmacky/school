from string import ascii_uppercase as letters

def base10(num: str) -> bool:
    return not any(s in letters for s in num)

file = open("24-307.txt")
text = file.readline().replace('+', '*')
# text = "45*4B*12*A5*7J**6B*78*6N*789*B*65*45666*66B"

val = ''
max_val = ''
for num in text.split('*'):
    if len(num) > 0:
        if num[0] != '0' or num == '0':
            if base10(num):
                val += num + '*'
            elif base10(num[:-1]) and num[-1] == 'B' and len(num) > 1:
                val += num + '*'
                max_val = max(max_val, val, key=len)
                val = ''
    else:
        val = ''

print(max_val)
print(len(max_val) - 1)
