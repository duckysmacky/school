file = open("1.txt")
student_count = int(file.readline())
students = []
for line in file:
    id, *marks = list(map(int, line.split()))
    students.append((marks.count(2), -(sum(marks) / len(marks)), id))
students.sort()

print(students)

last_top = students[int(student_count / 4) - 1]
print(last_top[2])
for student in students:
    if student[0] > 2:
        print(student[2])
        break
