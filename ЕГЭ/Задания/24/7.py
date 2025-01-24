file = open("24-275.txt")
text = file.readline()

rep = "XYZ"
filler = ''
msg = ''
max_msg = ''
for i in range(len(text) - 2):
    c = text[i]
    if c in rep:
        if len(msg) > 0:
            if (filler[-1] == 'Z' and c == 'X') or \
               (filler[-1] == 'Y' and c == 'Z') or \
               (filler[-1] == 'X' and c == 'Y'):
                max_msg = max(max_msg, msg, key=len)
                msg = ''
            else:
                msg += c
        else:
            filler += c
    else:
        msg += c
    
print(len(max_msg))
