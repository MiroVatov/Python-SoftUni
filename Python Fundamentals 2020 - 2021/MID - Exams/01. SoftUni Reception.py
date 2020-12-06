total_efficiency = 0
time = 0
for i in range(3):
    emp_efficiency = int(input())
    total_efficiency += emp_efficiency

employees_left = int(input())

while employees_left > 0:
    time += 1
    if time % 4 == 0:
        continue
    employees_left -= total_efficiency


print(f"Time needed: {time}h.")