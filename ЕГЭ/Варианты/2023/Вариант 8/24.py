file = open("Задание 24/24.txt")
text = file.readline()
text_lens = [len(t) for t in text.split(' ') if len(t) > 0]
print(min(text_lens))