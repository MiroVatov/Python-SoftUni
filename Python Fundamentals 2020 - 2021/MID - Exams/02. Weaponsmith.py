weapon_particles = input().split("|")

command = input()

while command != "Done":
    token = command.split()
    move = token[0] + ' ' + token[1]
    if move == "Move Left":
        index = int(token[2])
        if index < len(weapon_particles) and index > 0 :
            weapon_particles[index], weapon_particles[index - 1] = weapon_particles[index - 1], weapon_particles[index]

    elif move == "Move Right":
        index = int(token[2])
        if index < len(weapon_particles) and not index == len(weapon_particles) - 1:
            weapon_particles[index], weapon_particles[index + 1] = weapon_particles[index + 1], weapon_particles[index]

    elif move == "Check Even":
        evens = weapon_particles[::2]
        print(' '.join(evens))
    elif move == "Check Odd":
        odds = weapon_particles[1::2]
        print(f"{' '.join(odds)}")

    command = input()

print(f"You crafted {''.join(weapon_particles)}!")