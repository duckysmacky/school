import re

file = open("24-298.txt")
text = file.readline()
pattern = r"[1-9]\d*(?:[-*][1-9]\d*)+"
matches = re.findall(pattern, text)
print(len(max(matches, key=len)))
