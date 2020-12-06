import math

biscuits_per_day = int(input())
workers_qty = int(input())
amount_to_beat = int(input())

total_biscuits = 0

for days in range(1, 30 + 1):

    if days % 3 == 0:
        lower_biscuits = (biscuits_per_day * 0.75)
        total_biscuits += math.floor(workers_qty * lower_biscuits)
    else:
        total_biscuits += (workers_qty * biscuits_per_day)

print(f"You have produced {total_biscuits} biscuits for the past month.")



if total_biscuits > amount_to_beat:
    diff_perc = ((total_biscuits - amount_to_beat) / amount_to_beat) * 100
    print(f"You produce {diff_perc:.2f} percent more biscuits.")

elif amount_to_beat > total_biscuits:
    diff_perc = abs((total_biscuits - amount_to_beat) / amount_to_beat) * 100
    print(f"You produce {diff_perc:.2f} percent less biscuits.")