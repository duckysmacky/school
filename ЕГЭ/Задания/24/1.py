file = open("24-309.txt")
text = "FSRQ" + file.readline() + "FSRQ"
# text = "FSRQ**FSRQ**FSRQ***FSRQ***FSRQ***FSRQ"

indexes = [i for i in range(len(text)) if text[i:i + 4] == "FSRQ"]
step = 80 + 1
lens = []
for i in range(len(indexes) - step):
    lens.append(indexes[i + step] - indexes[i])
print(max(lens) + 2)
