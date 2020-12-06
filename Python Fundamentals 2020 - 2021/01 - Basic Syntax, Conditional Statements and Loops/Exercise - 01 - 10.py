allowed_quantity = int(input())
days = int(input())

ornament_set_price = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

christmas_spirit = 0
total_cost = 0

for day in range(1, days + 1):
    tree_garland_qty = 0
    tree_skirt_qty = 0
    if day % 11 == 0:
        allowed_quantity += 2

    if day % 2 == 0:
        total_cost += (ornament_set_price * allowed_quantity)
        christmas_spirit += 5
    if day % 3 == 0:
        tree_garland_qty += 1
        tree_skirt_qty += 1
        total_cost += (tree_skirt * allowed_quantity) + (tree_garland * allowed_quantity)
        christmas_spirit += 13
    if day % 5 == 0:
        total_cost += tree_lights * allowed_quantity
        christmas_spirit += 17
        if tree_skirt_qty == 1 and tree_garland_qty == 1:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += tree_skirt + tree_garland + tree_lights

    if day == days and day % 10 == 0:
        christmas_spirit -= 30


print(f'Total cost: {total_cost}')
print(f'Total spirit: {christmas_spirit}')