
users_dict = {}
contests_dict = {}

while True:
    command = input()
    if command == 'no more time':
        break
    token = command.split(' -> ')
    username = token[0]
    contest = token[1]
    points = int(token[2])

    if contest in contests_dict:
        if username in contests_dict[contest]:
            if points > contests_dict[contest][username]:
                contests_dict[contest][username] = points

        else:
            contests_dict[contest][username] = points
    else:
        contests_dict[contest] = {username: points}

for con, user in contests_dict.items():
    for u, p in user.items():
        if u not in users_dict:
            users_dict[u] = p
        else:
            users_dict[u] += p

for con, user in contests_dict.items():
    print(f'{con}: {len(user)} participants')
    counter = 0
    for u, po in sorted(user.items(), key=lambda x: (-x[1], x[0])):
        counter += 1
        print(f'{counter}. {u} <::> {po}')
num = 0
print('Individual standings:')
for person, po in sorted(users_dict.items(), key=lambda x: (- x[1], x[0])):
    num += 1
    print(f'{num}. {person} -> {po}')
