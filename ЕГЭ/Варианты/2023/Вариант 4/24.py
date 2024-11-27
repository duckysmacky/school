file = open("24.txt")
text = file.readline()

seqs = []
cnt_x, cnt_y = 0, 0
buff = ''
for i in range(len(text)):
    if text[i] == 'X':
        cnt_x += 1
    if text[i] == 'Y':
        cnt_y += 1
    if cnt_x > 5 or cnt_y > 5:
        seqs.append(buff)
        buff = ''
        cnt_x, cnt_y = 0, 0
    else:
        buff += text[i]
print([(s.count('X'), s.count('Y')) for s in seqs])
print(len(max(seqs, key=len)))