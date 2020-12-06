students_count = int(input())
total_grades = 0
excelent_count = 0
good_count = 0
average_count = 0
fail_count = 0
all_grades = 0

for student in range(1, students_count + 1):
    grade = float(input())
    if grade >= 5.00:
        excelent_count += 1
    elif 4.00 <= grade <= 4.99:
        good_count += 1
    elif 3.00 <= grade <= 3.99:
        average_count += 1
    elif grade < 3.00:
        fail_count += 1
    total_grades += grade
    all_grades +=1

perc_excelent = (excelent_count / all_grades) * 100
perc_good = (good_count / all_grades) * 100
perc_average = (average_count / all_grades) * 100
perc_fail = (fail_count / all_grades) * 100
total_average = total_grades / all_grades

print(f'Top students: {perc_excelent:.2f}%')
print(f'Between 4.00 and 4.99: {perc_good:.2f}%')
print(f'Between 3.00 and 3.99: {perc_average:.2f}%')
print(f'Fail: {perc_fail:.2f}%')
print(f'Average: {total_average:.2f}')