def valid_water(w_level, w_value, w_avail, cool_cells):
    if w_value in range(81, 126) and w_level == "High" and w_avail >= w_value:
        w_avail -= w_value
        cool_cells.append(w_value)
        return cool_cells, w_avail

    elif w_value in range(51, 81) and w_level == "Medium" and w_avail >= w_value:
        w_avail -= w_value
        cool_cells.append(w_value)
        return cool_cells, w_avail

    elif w_value in range(1, 51) and w_level == "Low" and w_avail >= w_value:
        w_avail -= w_value
        cool_cells.append(w_value)
        return cool_cells, w_avail


HIGH = range(81, 125 + 1)
MEDIUM = range(51, 80 + 1)
LOW = range(1, 50 + 1)

total_effort = 0
cooled_cells = []

fire_cells = input().split("#")
water_available = int(input())

for water in fire_cells:
    token = water.split(" = ")
    water_level = token[0]
    water_value = int(token[1])
    current_effort = 0

    if valid_water(water_level, water_value, water_available, cooled_cells):
        cooled_cells = cooled_cells
        water_available -= water_value
        current_effort = water_value * 0.25
        total_effort += current_effort

    if water_available <= 0:
        break

print(f"Cells:")
for w in cooled_cells:
    print(f" - {w}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(cooled_cells)}")