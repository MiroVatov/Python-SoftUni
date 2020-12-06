number_of_students = int(input())
excellent_students = 0
good_students = 0
average_students = 0
poor_students = 0
total_students = 0
total_grade = 0.0
for i in range(1 , number_of_students + 1):
    student_grade = float(input())

    if student_grade >= 5.00:
        excellent_students += 1
    elif 4.00 <= student_grade <= 4.99:
        good_students += 1
    elif 3.00 <= student_grade <= 3.99:
        average_students += 1
    elif 2.00 <= student_grade <= 2.99:
        poor_students += 1

    total_grade += student_grade
total_students = excellent_students + good_students + average_students + poor_students
avergage_grade = total_grade / total_students
perc_excellent_students = (excellent_students / total_students) * 100
perc_good_students = (good_students / total_students) * 100
perc_average_students = (average_students / total_students) * 100
perc_poor_students = (poor_students / total_students) * 100

print(f'Top students: {perc_excellent_students:.2f}%')
print(f'Between 4.00 and 4.99: {perc_good_students:.2f}%')
print(f'Between 3.00 and 3.99: {perc_average_students:.2f}%')
print(f'Fail: {perc_poor_students:.2f}%')
print(f'Average: {avergage_grade:.2f}')