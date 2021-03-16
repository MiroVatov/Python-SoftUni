from collections import deque

materials = list(map(int, input().split()))  #  we take the last material -> pop
magic_levels = deque(map(int, input().split()))  # we take the first magic level -> popleft

# presents_dict = {
#                 'Doll': [150, 0, False],
#                 'Wooden train': [250, 0, False],
#                 'Teddy bear': [300, 0, False],
#                 'Bicycle': [300, 0, False],
#                 }


# DOLL = [150, 0, False]
# WOODEN_TRAIN = [250, 0, False]
# TEDDY_BEAR = [300, 0, False]
# BICYCLE = [400, 0, False]

doll_dict = {'magic_needed': 150, 'quantity_produced': 0, 'success': False}
wooden_train_dict = {'magic_needed': 250, 'quantity_produced': 0, 'success': False}
teddy_bear_dict = {'magic_needed': 300, 'quantity_produced': 0, 'success': False}
bicycle_dict = {'magic_needed': 400, 'quantity_produced': 0, 'success': False}


# 1-st case -> if (product of mul of the mat. and the magic) is equal to one of the presents -> remove both (magic and material) and vreate a present.
# 2-nd case -> if (product of mul of the mat. and the magic) is negative number -> sum the values of prod and magic, remove the both and the result should be added to the materials.
# 3-rd case -> If the (product of mul of the mat. and the magic) doesn’t equal one of the magic levels in the table and is a positive number, remove only the magic value and increase the material value with 15.
# 4-th case -> If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents

# STOP cycle -> Stop crafting presents when you run out of boxes of materials or magic level values

# Your task is considered done if you manage to craft either one of the pairs - a doll and a train or a teddy bear and a bicycle

while materials and magic_levels:

    current_material = materials.pop()
    current_magic = magic_levels.popleft()

    # TODO check if the conditions for 0 should be moved on the bottom of the code

    if current_magic == 0 and current_material == 0:
        continue
    elif current_magic == 0:
        materials.append(current_material)
        continue
    elif current_material == 0:
        magic_levels.appendleft(current_magic)
        continue

    product_from_magic_and_material = current_material * current_magic

    if product_from_magic_and_material == doll_dict['magic_needed']:
        doll_dict['quantity_produced'] += 1
        doll_dict['success'] = True
        continue
    elif product_from_magic_and_material == wooden_train_dict['magic_needed']:
        wooden_train_dict['quantity_produced'] += 1
        wooden_train_dict['success'] = True
        continue
    elif product_from_magic_and_material == teddy_bear_dict['magic_needed']:
        teddy_bear_dict['quantity_produced'] += 1
        teddy_bear_dict['success'] = True
        continue
    elif product_from_magic_and_material == bicycle_dict['magic_needed']:
        bicycle_dict['quantity_produced'] += 1
        bicycle_dict['success'] = True
        continue

    if product_from_magic_and_material < 0:
        product_from_magic_and_material = current_material + current_magic
        materials.append(product_from_magic_and_material)

    elif product_from_magic_and_material > 0:
        current_material += 15
        materials.append(current_material)


success = False

if doll_dict['success'] is True and wooden_train_dict['success'] is True:
    success = True
if teddy_bear_dict['success'] is True and bicycle_dict['success'] is True:
    success = True

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")

if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

presents_dict = {'Doll': doll_dict['quantity_produced'], 'Wooden train': wooden_train_dict['quantity_produced'],
                 'Teddy bear': teddy_bear_dict['quantity_produced'], 'Bicycle': bicycle_dict['quantity_produced']}

for present, quantity in sorted(presents_dict.items()):
    if quantity > 0:
        print(f"{present}: {quantity}")

