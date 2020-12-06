contest_info = input().split(":")
contest_dict = {}

while contest_info[0] != "end of contests":
    contest = contest_info[0]
    password = contest_info[1]
    contest_dict[contest] = password
    contest_info = input().split(":")

contest_info_two = input().split("=>")
contest_courses = {}
contest_points = {}
last_points = 0

while contest_info_two[0] != "end of submissions":

    contest = contest_info_two[0]
    password = contest_info_two[1]
    username = contest_info_two[2]
    points = int(contest_info_two[3])

    if contest in contest_dict:
        if password == contest_dict[contest]:
            if username not in contest_courses.keys():
                contest_courses[username] = {}
                contest_points[username] = points
                if contest not in contest_courses[username].keys():
                    contest_courses[username] = {contest: points}

                else:
                    if points >= contest_courses[username][contest]:
                        contest_courses[username][contest] = points

            else:
                if contest not in contest_courses[username].keys():
                    contest_points[username] += points
                    contest_courses[username][contest] = points
                elif contest in contest_courses[username].keys():
                    if points >= contest_courses[username][contest]:
                        contest_courses[username][contest] = points
                        contest_points[username] = points


    contest_info_two = input().split("=>")


max_points_user = max(contest_points, key=contest_points.get)
max_points_value = max(contest_points.values())

print(f"Best candidate is {max_points_user} with total {max_points_value} points.")

sorted_contest_dict = dict(sorted(contest_courses.items(), key=lambda x: x[0]))
final_sorted_contest_dict = res = {key : dict(sorted(val.items(), key = lambda ele: -(ele[1])))
       for key, val in sorted_contest_dict.items()}

print("Ranking:")

for key, value in final_sorted_contest_dict.items():
    print(key)
    for k, v in value.items():
        print(f"#  {k} -> {v}")