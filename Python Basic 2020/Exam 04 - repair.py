import math
wall_height = int(input())
wall_width = int(input())
percent_notbe_painted = int(input())
command = input()

total_area = (wall_width * wall_height * 4)
total_area = total_area - (percent_notbe_painted * total_area / 100)
while command != 'Tired!':
    liters_paint = int(command)
    total_area -= liters_paint

    if total_area <= 0:
        break
    command = input()

if command == 'Tired!':
    print(f'{math.ceil(total_area)} quadratic m left.')
elif total_area < 0:

    print(f'All walls are painted and you have {abs(math.ceil(total_area))} l paint left!')
elif total_area >= 0:
    print(f'All walls are painted! Great job, Pesho!')