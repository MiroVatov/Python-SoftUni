
command = input().split("-")

user_dict = {}
points_dict = {}

while command[0] != "exam finished":
    username = command[0]
    language = command[1]
    if language == "banned":
        user_dict.pop(username)
        command = input().split("-")
        continue
    points = int(command[2])

    if username not in user_dict:
        user_dict[username] = [points]
    else:
        user_dict[username] += [points]
    if language not in points_dict:
        points_dict[language] = [points]
    else:
        points_dict[language] += [points]

    command = input().split("-")

sorted_user_duct = dict(sorted(user_dict.items(), key= lambda x: (- max(x[1]), x[0])))
sorted_points_dict = dict(sorted(points_dict.items(), key= lambda x: (- len(x), x[0])))

print(f"Results:")

for k, v in sorted_user_duct.items():
    max_val = max(v)
    print(f"{k} | {max_val}")

print(f"Submissions:")

for a, b in sorted_points_dict.items():
    print(f"{a}", end=' - ')
    print(f"{len(b)}")


