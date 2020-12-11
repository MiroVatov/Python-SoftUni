
contest_dict = {}

while True:
    command = input().split(':')
    if command[0] == 'end of contests':
        break
    cont = command[0]
    password = command[1]
    contest_dict[cont] = password

users_contests_dict = {}

while True:
    users_info = input()
    if users_info == 'end of submissions':
        break
    token = users_info.split('=>')
    contest = token[0]
    password = token[1]
    username = token[2]
    points = int(token[3])

    if contest in contest_dict:
        if password == contest_dict[contest]:
            if username in users_contests_dict:
                if contest in users_contests_dict[username]:
                    if points > users_contests_dict[username][contest]:
                        users_contests_dict[username][contest] = points
                else:
                    users_contests_dict[username][contest] = points
            else:
                users_contests_dict[username] = {contest: points}

user_points_dict = {}

for user, cont in users_contests_dict.items():
    for k, po in cont.items():
        if user not in user_points_dict:
            user_points_dict[user] = po
        else:
            user_points_dict[user] += po

max_points = -1_000_000
max_user = ''

for u, p in user_points_dict.items():
    if p > max_points:
        max_points = p
        max_user = u

print(f'Best candidate is {max_user} with total {max_points} points.')

print('Ranking:')
for key, value in sorted(users_contests_dict.items(), key=lambda x: x[0]):
    print(f'{key}')
    for u, p in sorted(value.items(), key=lambda x: (-x[1])):
        print(f'#  {u} -> {p}')

