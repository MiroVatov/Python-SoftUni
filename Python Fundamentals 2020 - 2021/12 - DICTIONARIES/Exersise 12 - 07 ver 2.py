n = int(input())

students_dict = {}

for i in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in students_dict:
        students_dict[student_name] = [student_grade]
    else:
        students_dict[student_name] += [student_grade]

# with dictionary_comprehension
get_average = lambda x: sum(x) / len(x)

new_dict = {key: get_average(value) for (key, value) in students_dict.items() if get_average(value) >= 4.5}

sorted_dict = dict(sorted(new_dict.items(), key=lambda x: x[1], reverse=True ))

for s, g in sorted_dict.items():
    print(f"{s} -> {g:.2f}")
