from string import ascii_uppercase

file = open("24-294.txt")
text = file.readline()
#text = "7AA6691607610760721Y0721607F079G7H"

for ch in ascii_uppercase:
    text = text.replace(ch, '*')
text = text.split('*')

print(text)

max_sub = 0
for sub in text:
    sub = '7' + sub + '7'
    i7 = [i for i in range(len(sub)) if sub[i] == '7']
    print(sub, i7)

    step = 80 + 1
    cnts = [0]
    for i in range(len(i7) - step):
        cnts.append(i7[i + step] - i7[i])
    max_sub = max(max_sub, max(cnts))

print(max_sub - 1)
