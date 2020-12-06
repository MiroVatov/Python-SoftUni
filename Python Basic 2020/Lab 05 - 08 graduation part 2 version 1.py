student = input()
level = 1
total_grade = 0
cut = 0

while level <= 12:
    grades = float(input())
    if grades >= 4:
        level += 1
        total_grade += grades
    elif grades < 4:
        cut += 1
        if cut >= 2:
            print(f'{student} has been excluded at {level} grade')
            break

if level >= 12:
    average_grade = total_grade / 12
    print(f'{student} graduated. Average grade: {average_grade:.2f}')