student = input()
level = 1
total_grade = 0

while level <= 12:
    grades = float(input())

    if grades < 4:
        continue

    total_grade += grades
    level += 1

average_grade = total_grade / 12
print(f'{student} graduated. Average grade: {average_grade:.2f}')