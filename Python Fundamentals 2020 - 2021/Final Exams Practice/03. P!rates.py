
target_cities_dict = {}

while True:

    command = input()

    if command == "Sail":
        break
    token = command.split("||")
    town = token[0]
    population = int(token[1])
    gold = int(token[2])

    if town not in target_cities_dict:
        target_cities_dict[town] = [population, gold]
    else:
        target_cities_dict[town][0] += population
        target_cities_dict[town][1] += gold

while True:

    command = input()

    if command == "End":
        break

    token = command.split("=>")

    if token[0] == "Plunder":
        town = token[1]
        people = int(token[2])
        gold = int(token[3])

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        target_cities_dict[town][0] -= people
        target_cities_dict[town][1] -= gold

        if target_cities_dict[town][0] <= 0 or target_cities_dict[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del target_cities_dict[town]

    elif token[0] == "Prosper":
        town = token[1]
        gold = int(token[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        else:
            target_cities_dict[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {target_cities_dict[town][1]} gold.")

sorted_dict = dict(sorted(target_cities_dict.items(), key=lambda x: (- x[1][1], x[0])))

if len(target_cities_dict) > 0:
    print(f"Ahoy, Captain! There are {len(target_cities_dict)} wealthy settlements to go to:")

    for key, val in sorted_dict.items():
        print(f"{key} ->", end= ' ')
        print(f"Population: {val[0]} citizens, Gold: {val[1]} kg")

else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")



