
pirate_ship_good = True
warship_good = True
pirateship_status = [int(i) for i in input().split(">")]
warship_status = [int(i) for i in input().split(">")]
max_health = int(input())


while True:
    command = input()
    if command == "Retire":
        break
    token = command.split()
    action = token[0]
    if action == "Fire":
        index = int(token[1])
        damage = int(token[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if int(warship_status[index]) <= 0:
                print(f'You won! The enemy ship has sunken.')
                warship_good = False
                break

    elif action == "Defend":
        start = int(token[1])
        end = int(token[2])
        damage = int(token[3])
        if 0 <= start < len(pirateship_status) and 0 <= end < len(pirateship_status):

            for i in range(start, end + 1):
                pirateship_status[i] -= damage
                if pirateship_status[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    pirate_ship_good = False
                    break

    elif action == "Repair":
        index = int(token[1])
        health = int(token[2])
        if 0 <= index < len(pirateship_status):
            if (pirateship_status[index] + health) < max_health:
                pirateship_status[index] += health
            else:
                pirateship_status[index] = max_health

    elif action == "Status":
        sections_for_repair = 0
        repair_sec = int(max_health * 0.20)
        for i in range(len(pirateship_status)):
            if int(pirateship_status[i]) < repair_sec:
                sections_for_repair += 1
        print(f"{sections_for_repair} sections need repair.")

if warship_good and pirate_ship_good:
    print(f"Pirate ship status: {sum(pirateship_status)}")
    print(f"Warship status: {sum(warship_status)}")

