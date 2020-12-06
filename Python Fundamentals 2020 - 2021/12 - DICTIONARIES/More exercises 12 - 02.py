
contest_dict = {}
user_points_dict = {}

while True:
    command = input()

    if command == "no more time":
        break

    token = command.split("->")
    username = token[0].strip()
    contest = token[1].strip()
    points = int(token[2])

    if contest in contest_dict:
        if username in contest_dict[contest]:
            if points > contest_dict[contest][username]:
                contest_dict[contest][username] = points
                user_points_dict[username] = points
            else:
                contest_dict[contest][username] += points
                user_points_dict[username] += points

        else:
            contest_dict[contest][username] = points
            if username in user_points_dict:
                user_points_dict[username] += points
            else:
                user_points_dict[username] = points
    else:
        contest_dict[contest] = {username: points}
        if username in user_points_dict:
            user_points_dict[username] += points
        else:
            user_points_dict[username] = points


sorted_points_dict = dict(sorted(user_points_dict.items(), key=lambda x: (-x[1],x[0])))

sorted_contest_dict = res = {key : dict(sorted(val.items(), key = lambda ele: -(ele[1])))
       for key, val in contest_dict.items()}


for x, y in sorted_contest_dict.items():
    counter = 0
    print(f"{x}: {len(y)} participants")
    for v, n in y.items():

        counter += 1
        print(f"{counter}. {v} <::> {n}")

print(f"Individual standings:")
counter2 = 0
for k, v in sorted_points_dict.items():
    counter2 += 1
    print(f"{counter2}. {k} -> {v}")