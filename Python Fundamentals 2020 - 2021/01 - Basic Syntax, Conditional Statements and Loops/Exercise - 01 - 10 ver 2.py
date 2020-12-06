quantity = int(input())
days = int(input())

ornament = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

budget = 0
spirit_total = 0
step = 0

while days > 0:

    step += 1
    if step % 11 == 0:
        quantity += 2
    if step % 2 == 0:
        budget += ornament * quantity
        spirit_total += 5
    if step % 3 == 0:
        budget += (tree_skirt + tree_garland) * quantity
        spirit_total += 13
    if step % 5 == 0:
        budget += tree_lights * quantity
        spirit_total += 17
        if step % 3 == 0:
            spirit_total += 30
    days -= 1
    if step % 10 == 0:
        spirit_total -= 20
        budget += tree_skirt + tree_garland + tree_lights

        if days == 0:
            spirit_total -= 30


print (f'Total cost: {budget}')
print (f'Total spirit: {spirit_total}')