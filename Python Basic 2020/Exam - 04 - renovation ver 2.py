import math
wall_height = int(input())
wall_width = int(input())
percent_notbe_painted = int(input())
command = input()
paint_left = 0
total_paint = 0
total_area = (wall_width * wall_height * 4)
total_area = total_area - (percent_notbe_painted * total_area / 100)

while command != 'Tired!':
    liters_paint = int(command)
    total_area -= liters_paint
    total_paint += liters_paint
    if total_area <= 0:
        break
    command = input()
paint_left = total_paint - total_area
if command == 'Tired!':
    print(f'{math.ceil(total_area)} quadratic m left.')
elif total_area < 0:

    print(f'All walls are painted and you have {abs(math.ceil(total_area))} l paint left!')
elif total_area >= 0:
    print(f'All walls are painted! Great job, Pesho!')

print(paint_left)