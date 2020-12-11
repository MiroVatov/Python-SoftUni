
number_of_plants = int(input())

plants_dict = {}

for n in range(number_of_plants):
    plants_command = input().split("<->")

    plant_name = plants_command[0]
    rarity = int(plants_command[1])

    if plant_name not in plants_dict:
        plants_dict[plant_name] = [[rarity], []]
    else:
        plants_dict[plant_name] = [[rarity], []]

while True:

    command = input()

    if command == "Exhibition":
        break
    command = command.split(": ")

    if command[0] == "Rate":
        token = command[1].split(" - ")
        plant = token[0]
        rating = int(token[1])

        if plant not in plants_dict:
            print("error")
        else:
            plants_dict[plant][1] += [rating]

    elif command[0] == "Update":
        token = command[1].split(" - ")
        plant = token[0]
        new_rarity = int(token[1])

        if plant not in plants_dict:
            print("error")
        else:
            plants_dict[plant][0] = [new_rarity]

    elif command[0] == "Reset":
        plant = command[1]

        if plant not in plants_dict:
            print("error")
        else:
            plants_dict[plant][1].clear()


for sub, val in plants_dict.items():
    if len(val[1]) > 0:
        val[1] = [sum(val[1])/len(val[1])]
    else:
        val[1] = [0]


for k, v in plants_dict.items():
    plants_dict[k] = [inner for item in v for inner in item]

sorted_plants_dict = dict(sorted(plants_dict.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True))

print(f"Plants for the exhibition:")
for plants, values in sorted_plants_dict.items():
    print(f"- {plants}; Rarity: {values[0]}; Rating: {values[1]:.2f}")