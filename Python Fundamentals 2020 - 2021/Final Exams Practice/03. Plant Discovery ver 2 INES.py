n = int(input())
plants = {}


for _ in range(n):
    plant, rarity = input().split('<->')
    plants[plant] = {'rarity': int(rarity), 'ratings': []}

data = input()

while not data == "Exhibition":
    command, value = data.split(': ')
    try:
        if command == "Rate":
            plant, rating = value.split(" - ")
            plants[plant]['ratings'].append(int(rating))
        elif command == "Update":
            plant, rarity = value.split(" - ")
            plants[plant]['rarity'] = int(rarity)
        elif command == "Reset":
            plant = value
            plants[plant]['ratings'].clear()
    except:
        print("error")
    data = input()

for plant_name, plants_data in plants.items():
    if plants[plant_name]['ratings']:
        plants[plant_name]['avg'] = sum(plants[plant_name]['ratings'])/len(plants[plant_name]['ratings'])
    else:
        plants[plant_name]['avg'] = 0

sorted_plants = sorted(plants.items(), key=lambda x: (x[1]['rarity'], x[1]['avg']), reverse=True)

print("Plants for the exhibition:")
for plant_name, value in sorted_plants:
    print(f"- {plant_name}; Rarity: {value['rarity']}; Rating: {value['avg']:.2f}")