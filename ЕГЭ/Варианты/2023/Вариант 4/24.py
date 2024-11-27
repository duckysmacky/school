file = open("24.txt")
text = file.readline()

seqs = []
cnt = 0
buff = ""
for i in range(len(text)):
    if text[i] == 'X' or text[i] == 'Y':
        cnt += 1
    if cnt == 5:
        seqs.append(buff)
        buff = ''
        cnt = 0
    else:
        buff += text[i]
print(len(max(seqs, key=len)))