animal_dict = {}
areas_dict = {}

command = input().split(":")

while command[0] != "Last Info":

    action = command[0]
    animal_name = command[1]
    food = int(command[2])
    area = command[3]
    if action == "Add":
        if animal_name not in animal_dict:
            animal_dict[animal_name] = food
            if area not in areas_dict:
                areas_dict[area] = 1
            else:
                areas_dict[area] += 1
        else:
            animal_dict[animal_name] += food

    elif action == "Feed":
        if animal_name in animal_dict:
            animal_dict[animal_name] -= food
            if animal_dict[animal_name] <= 0:
                print(f"{animal_name} was successfully fed")
                animal_dict.pop(animal_name)
                areas_dict[area] -= 1

    command = input().split(":")

sorted_dict_area = dict(sorted(areas_dict.items(), key=lambda x: (- x[1], x[0])))
sorted_dict_animals = dict(sorted(animal_dict.items(), key=lambda y: y[1], reverse=True))

print(f"Animals:")
for k, v in sorted_dict_animals.items():
    print(f"{k} -> {v}g")

print(f"Areas with hungry animals:")

for k, v in sorted_dict_area.items():
    if v > 0:
        print(f"{k} : {v}")