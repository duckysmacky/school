import re

file = open("24-274.txt")
text = file.readline()
pattern = r"(?:PC|CSGO)+"
matches = re.findall(pattern, text)
print(len(max(matches, key=len)))
