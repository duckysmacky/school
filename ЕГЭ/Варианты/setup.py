from os import makedirs
from os.path import exists

print("Генерация шаблона варианта")
category = input("Раздел (год, автор или др.): ")
number = input("Номер варианта: ")
dir = f"{category}/Вариант {number}"

print(f"{dir}/!answers.txt")
if not exists(dir):
    makedirs(dir)
answers_file = open(f"{dir}/!answers.txt", 'w')

for i in range(27):
    answers_file.write(f"{i + 1} - {'\n' if i < 26 else ''}")

python_files = [2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 23, 24, 25, 26]
for file in map(lambda x: f"{x}.py", python_files):
    f = open(f"{dir}/{file}", 'w')
    f.close()