import re

file = open("24-275.txt")
text = file.readline()
text = "XYZXYZXYUSEFULMESSAGEZXYZXYZXYZAVERYUSEFULMESSAGEZXYZXYZXYZ"

filler = r"(?:[XYZ]{1,3})+"
pattern = rf"{filler}([A-Z]+?){filler}"
matches = re.findall(pattern, text)
print(matches)
