command = input().split(":")
courses_dict = {}


while command[0] != "end":
    course = command[0].strip()
    student = command[1]

    if course not in courses_dict:
        courses_dict[course] = [student]
    else:
        courses_dict[course] += [student]

    command = input().split(":")

sorted_courses = dict(sorted(courses_dict.items(), key=lambda c: len(c[1]), reverse=True))

for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")

    for st in sorted(value):
        print(f"--{st}")