letters = ["I", "V", "A", "N"]
word = ["0"] * 5
count = 0

#for x in range(len(letters)**len(word)):
for pos in range(5):
    for l in range(4):
        word[pos] = letters[l]
        print(word)
                
print(count)