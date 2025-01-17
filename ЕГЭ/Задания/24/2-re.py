import re

file = open("24-307.txt")
text = file.readline()
num = r"(?:[1-9]\d*|0)"
pattern = rf"{num}(?:[+*]{num})*B"
matches = list(map(''.join, re.findall(pattern, text)))

print(len(max(matches, key=len)))
