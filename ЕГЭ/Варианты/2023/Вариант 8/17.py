file = open("Задание 17/17.txt")
nums = list(map(int, [l for l in file if '4' in l]))
print(len(nums), max(nums))