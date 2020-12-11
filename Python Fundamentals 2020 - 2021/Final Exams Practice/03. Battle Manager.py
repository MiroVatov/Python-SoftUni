battles_dict = {}

while True:
    command = input()
    if command == 'Results':
        break

    token = command.split(':')
    action = token[0]
    if action == 'Add':
        person = token[1]
        health = int(token[2])
        energy = int(token[3])
        if person not in battles_dict:
            battles_dict[person] = {'health': health, 'energy': energy}
        else:
            battles_dict[person]['health'] += health

    elif action == 'Attack':
        attacker = token[1]
        defender = token[2]
        damage = int(token[3])
        if attacker in battles_dict and defender in battles_dict:
            battles_dict[defender]['health'] -= damage
            if battles_dict[defender]['health'] <= 0:
                del battles_dict[defender]
                print(f"{defender} was disqualified!")
            battles_dict[attacker]['energy'] -= 1
            if battles_dict[attacker]['energy'] <= 0:
                del battles_dict[attacker]
                print(f"{attacker} was disqualified!")

    elif action == 'Delete':
        username = token[1]
        if username == 'All':
            battles_dict.clear()
        else:
            if username in battles_dict:
                del battles_dict[username]

print(f"People count: {len(battles_dict)}")

sorted_dict = dict(sorted(battles_dict.items(),key=lambda x:(-x[1]['health'], x[0])))
for key, value in sorted_dict.items():
    print(f"{key} - {value['health']} - {value['energy']}")