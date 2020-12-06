HIGH = range(81, 125 + 1)
MEDIUM = range(51, 80 + 1)
LOW = range(1, 50 + 1)

total_effort = 0
fire_cells = input().split("#")
water_available = int(input())
cooled_cells = []

for water in fire_cells:
    token = water.split(" = ")
    water_level = token[0]
    water_value = int(token[1])
    fire_valid = False

    if water_level == "High" and water_value in HIGH and water_available >= water_value:
        fire_valid = True

    elif water_level == "Medium" and water_value in MEDIUM and water_available >= water_value:
        fire_valid = True

    elif water_level == "Low" and water_value in LOW and water_available >= water_value:
        fire_valid = True

    if fire_valid:
        water_available -= water_value
        current_effort = water_value * 0.25
        total_effort += current_effort
        cooled_cells.append(water_value)

    if water_available <= 0:
        break

print(f"Cells:")
for w in cooled_cells:
    print(f" - {w}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(cooled_cells)}")