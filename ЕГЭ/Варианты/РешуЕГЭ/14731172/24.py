import re
with open("14731172/24_demo.txt") as f:
    text = f.readline()

found = re.findall(r"(?:XYZ)+(?:XY|X)", text)
print(found)
length = map(lambda x: len(x), found)
print(max(length))