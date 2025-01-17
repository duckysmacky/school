import re

file = open("24-296.txt")
text = file.readline()

letters = r"[ABCDEF]*?"
pair = r"(?:AF){201}"
pattern = rf"{letters}{pair}{letters}"
matches = re.findall(pattern, text)

print(matches)
print(pattern)
print(len(min(matches, key=len)))
