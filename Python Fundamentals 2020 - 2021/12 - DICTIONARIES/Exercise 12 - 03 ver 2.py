
key_materials = {
    "fragments": 0,
    "shards": 0,
    "motes": 0
}

legendary_items = {
    "fragments": "Valanyr",
    "shards": "Shadowmourne",
    "motes": "Dragonwrath"
}

junks = {}
winner = ""

while winner == "":
    args = input().lower().split()

    for i in range(0, len(args), 2):
        quantity = int(args[i])
        material = args[i + 1]
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                winner = material
                break
        else:
            if material not in junks:
                junks[material] = 0
            junks[material] += quantity

key_materials[winner] -= 250
winner_item = legendary_items[winner]

print(f"{winner_item} obtained!")

sorted_materials = dict(sorted(key_materials.items(),key= lambda x: (- x[1], x[0])))
sorted_junks = sorted(junks.items(), key= lambda x: x[0])

for a , b in sorted_materials.items():
    print(f"{a}: {b}")

for c , d in sorted_junks:
    print(f"{c}: {d}")