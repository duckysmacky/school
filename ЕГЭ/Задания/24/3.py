file = open("24-296.txt")
text = "AF" + file.readline() + "AF"
# text = "AF**AF*AF***AF***AF***AF"
#       0123456789 -> 5
indexes = [i for i in range(len(text)) if text[i:i + 2] == "AF"]
step = 201 - 1
lens = []
for i in range(len(indexes) - step):
    lens.append(indexes[i + step] - indexes[i])
print(max(lens))
