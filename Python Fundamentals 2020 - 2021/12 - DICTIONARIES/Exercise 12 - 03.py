success = False

key_materials = {}
junks = {}
legendary_items = ["shards", "fragments", "motes"]
command = input().split(" ")
while not success:
    for i in range(0, len(command), 2):

        key = command[i + 1]
        material = key.lower().strip()
        value = int(command[i])

        if material != "shards" and material != "fragments" and material != "motes":
            if material not in junks:
                junks[material] = 0
            junks[material] += value
        if material not in key_materials:
            key_materials[material] = 0
        key_materials[material] += value

        if material == "shards":
            if key_materials[material] >= 250:
                success = True
                key_materials[material] = key_materials[material] - 250
                print(f"Shadowmourne obtained!")
                break

        elif material == "fragments":
            if key_materials[material] >= 250:
                success = True
                key_materials[material] = key_materials[material] - 250
                print(f"Valanyr obtained!")
                break

        elif material == "motes":
            if key_materials[material] >= 250:
                success = True
                key_materials[material] = key_materials[material] - 250
                print(f"Dragonwrath obtained!")
                break

    if success:
        break

    command = input().split(" ")

lst = []

for x in legendary_items:
    if x not in key_materials:
        key_materials[x] = 0

for key, value in key_materials.items():
    if key in junks:
        lst.append(key)

for ind in lst:
    del key_materials[ind]

my_dict_sorted = sorted(key_materials.items(), key=lambda x: (- x[1], x[0]))
junks_sorted = sorted(junks.items(), key=lambda x: x[0])

for a, b in my_dict_sorted:
    print(f"{a}: {b}")
for c,  d in junks_sorted:
    print(f"{c}: {d}")



