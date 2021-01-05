num_of_grades = int(input())

students_dict = {}

for _ in range(num_of_grades):
    student_info = input().split()
    student_name = student_info[0]
    grade = float(student_info[1])
    if student_name not in students_dict:
        students_dict[student_name] = [grade]
    else:
        students_dict[student_name].append(grade)

for (stud, grades) in students_dict.items():
    avg_grade = sum(grades) / len(grades)
    # grades = ' '.join(map(lambda f: format(f, '.2f'), grades))  # format function that makes str formatted to float number, but it is still string
    grades = [f"{mark:.2f}" for mark in grades]
    print(f"{stud} -> {' '.join(grades)} (avg: {avg_grade:.2f})")