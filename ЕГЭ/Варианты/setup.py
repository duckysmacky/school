print("Генерация шаблона варианта")
year = input("Год: ")
number = input("Номер варианта: ")
dir = f"{year}/Вариант {number}"

print(f"{dir}/!answers.txt")
answers_file = open(f"{dir}/!answers.txt", 'w')
for i in range(27):
    answers_file.write(f"{i + 1} - \n")