file = open('24.txt')
text = file.readline()
text = 'AA***AA**A**A***A***A*****A***A**A***A**A'

indexes = [i for i in range(len(text)) if text[i] == 'A']
step = 2 + 1
cnts = []
for i in range(len(indexes) - step):
    cnts.append(indexes[i + step] - indexes[i])
print(min(cnts))
