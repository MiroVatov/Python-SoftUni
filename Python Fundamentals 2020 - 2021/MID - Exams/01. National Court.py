emp1 = int(input())
emp2 = int(input())
emp3 = int(input())
total_people_per_hour = emp1 + emp2 + emp3

total_people_count = int(input())

total_hours = 0

while True:
    if total_people_count <= 0:
        break

    total_hours += 1
    if total_hours % 4 == 0:
        continue
    else:
        total_people_count -= total_people_per_hour


print(f"Time needed: {total_hours}h.")