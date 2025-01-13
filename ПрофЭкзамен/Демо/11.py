def get_value(letter: str) -> int:
    alph = "АБВГДЕЁЗЖИЙКЛМНОПРСТУФХЦЧШЩъЫЬЭЮЯ"
    return alph.index(letter) + 1

def hash(password: str) -> int:
    n = 187
    H = 5
    for letter in password:
        H = ((H + get_value(letter)) ** 2) % n
    return H

passwords = [
    "КОЛЛИЗИЯ",
    "ПРОКСИФИКАЦИЯ",
    "БЕЗОПАСНОСТЬ",
    "АНАЛИТИК",
    "СИСТЕМА",
    "КРИПТОСТОЙКОСТЬ",
    "АДМИНИСТРИРОВАНИЕ",
    "УПРАВЛЕНИЕ",
    "ПРЕОБРАЗОВАНИЕ",
    "КЛАССИФИКАТОР"
]

for password in passwords:
    hash_val = hash(password)
    if hash_val == 26:
        print(password)