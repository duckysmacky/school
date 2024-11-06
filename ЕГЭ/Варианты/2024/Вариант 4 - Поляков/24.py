import re

file = open("24.txt")
text = file.readline()

pattern = re.compile(r"A[BCDE]+F")
found = re.findall(pattern, text)
print(len(min(found, key=len)))