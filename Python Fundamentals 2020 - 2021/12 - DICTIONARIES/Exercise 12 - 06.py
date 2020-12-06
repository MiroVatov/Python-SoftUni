
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


courses_dict_sorted = dict(sorted(courses_dict.items(), key = lambda x: - len(x[1])))

for k, v in courses_dict_sorted.items():

    print(f"{k}: {len(v)}")
    for n in sorted(v):
        print(f"--{n}")

