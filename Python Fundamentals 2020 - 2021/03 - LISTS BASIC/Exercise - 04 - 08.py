RANGE_HIGH = range(81, 126)
RANGE_MEDIUM = range(51, 81)
RANGE_LOW = range(1, 51)

fire_cells = input().split('#')

water = int(input())
total_effort = 0
total_fire = 0
final_lst = []

for i in fire_cells:
    tokens = i.split(" = ")
    fire_level = tokens[0]
    fire_cell_value = int(tokens[1])
    effort = 0

    if fire_level == "High":
        if fire_cell_value in RANGE_HIGH:
            if fire_cell_value <= water:

                effort = fire_cell_value * 0.25
        else:
            continue

    if fire_level == 'Medium':
        if fire_cell_value in RANGE_MEDIUM:
            if fire_cell_value <= water:

                effort = fire_cell_value * 0.25
        else:
            continue

    if fire_level == 'Low':
        if fire_cell_value in RANGE_LOW:
            if fire_cell_value <= water:
                effort = fire_cell_value * 0.25
        else:
            continue

    if fire_cell_value <= water:
        final_lst.append(fire_cell_value)
        total_fire += fire_cell_value
        total_effort += effort
        water -= fire_cell_value

print(f'Cells:')

for ind in final_lst:
    print(f' - {ind}')

print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')