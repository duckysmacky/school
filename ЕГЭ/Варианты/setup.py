from os import makedirs
from os.path import exists

print("Генерация шаблона варианта")
category = input("Раздел (год, автор или др.): ")
number = input("Номер варианта: ")
dir = f"{category}/Вариант {number}"

print(f"{dir}/!answers.txt")
if not exists(dir):
    makedirs(dir)
answers_file = open(f"{dir}/!answers", 'w')

for i in range(27):
    answers_file.write(f"{i + 1} - {'\n' if i < 26 else ''}")
