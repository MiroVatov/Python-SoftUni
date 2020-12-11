iterations = int(input())

flower_colection = {}
for discovored_flowers in range (iterations):
    plants = input().split("<->")
    plant = plants[0]
    rarity = int(plants[1])
    rating = 0
    if plant not in flower_colection:
        flower_colection[plant] = []
    flower_colection[plant].append(rarity)
    flower_colection[plant].append(rating)

plant_rating = {}
command = input()
while not command == "Exhibition":
    command = command.split((": "))
    action = command[0]

    if action == "Rate":
        plant, rating = command[1].split(" - ")
        rating = int(rating)
        if plant not in flower_colection:
            print("error")
        else:
            if plant not in plant_rating:
                plant_rating[plant] = []
            plant_rating[plant].append(rating)

    elif action == "Update":
        plant, new_rarity = command[1].split(" - ")
        new_rarity = int(new_rarity)
        if plant not in flower_colection:
            print("error")
        else:
            flower_colection[plant][0] = new_rarity

    else:
        plant = command[1]
        if plant not in flower_colection:
            print("error")
        else:
            plant_rating[plant].clear()

    command = input()
for key, value in plant_rating.items():
    if sum(value) == 0:
       value = 0
       # plant_rating[key] = value
    else:
        value = sum(value) / len(value)
        plant_rating[key] = value
    for plants, rarity in flower_colection.items():
        if plants == key:
            flower_colection[key][1] = value

flower_colection = dict(sorted(flower_colection.items(), key= lambda x: ( -x[1][0], -x[1][1] )))
print("Plants for the exhibition:")
for key, value in flower_colection.items():

    print(f"- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}")