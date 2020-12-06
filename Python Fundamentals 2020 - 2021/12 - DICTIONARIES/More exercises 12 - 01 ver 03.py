content_pass = {}
user_cours_points = {}
users_maxpoints = {}
while True:
    data_content = input()
    if data_content == "end of contests":
        break
    data = data_content.split(":")
    cours = data[0]
    pass_word = str(data[1])

    content_pass[cours] = pass_word

while True:
    next_data = input()
    if next_data == "end of submissions":
        break
    indexes = next_data.split("=>")
    content = indexes[0]
    password = indexes[1]
    username = indexes[2]
    points = indexes[3]
    if content in content_pass and password in content_pass[content]:
        if username not in user_cours_points:
            user_cours_points[username] = {}
            user_cours_points[username][content] = points
        elif content not in user_cours_points[username]:
            user_cours_points[username][content] = points
        else:
            if int(user_cours_points[username][content]) < (int(points)):
                user_cours_points[username][content] = (int(points))
                points = (int(points)) - user_cours_points[username][content]
                users_maxpoints[username] += points
                continue
            else:
                continue
        if username not in users_maxpoints:
            users_maxpoints[username] = int(points)

        else:
            users_maxpoints[username] += int(points)

user_cours_points = dict(sorted(user_cours_points.items(), key=lambda x: x[0]))
keys = [k for k in user_cours_points.keys()]
dict_value = [v for v in user_cours_points.values()]
dict_values = [dict(sorted(x.items(), key=lambda kv: kv[1], reverse=True)) for x in dict_value]
nesteddict = dict(zip(keys, dict_values))
nam, val = max(users_maxpoints.items(), key=lambda x: x[1])
print(f"Best candidate is {nam} with total {val} points.")
print("Ranking:")
for k, v in nesteddict.items():
    print(k)
    for n in v:
        print(f"#  {n} -> {v[n]}")