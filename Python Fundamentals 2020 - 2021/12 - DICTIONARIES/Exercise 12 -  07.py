n = int(input())

students_dict = {}

for i in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(student_grade)

new_dict = {}

for k, v in students_dict.items():
    avg = sum(v) / len(v)
    if avg < 4.50:
        continue
    new_dict[k] = avg

sorted_dict = dict(sorted(new_dict.items(), key=lambda x: x[1], reverse=True ))

for s, g in sorted_dict.items():
    print(f"{s} -> {g:.2f}")
