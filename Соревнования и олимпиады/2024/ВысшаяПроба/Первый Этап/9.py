import json

file_name = input()

file = open(file_name)
header = file.readline()
cipher = {}
for line in file:
    i, val, key = line.split(";")
    cipher[key.strip()] = val
print(cipher)

messages = []
for _ in range(4):
    messages.append(input())

decoded = {}
for i in range(len(messages)):
    text = messages[i]
    d_text = ""
    for j in range(len(text) - 1):
        pair = text[j:j + 2]
        if pair in cipher:
            d_text += cipher[pair] + " "
            j += 1
    decoded[i] = d_text

json_file = open("tabula_rasa.json", 'w')
json_file.write(json.dumps(decoded, indent=4))