car_race = [int(i) for i in input().split()]

finish = len(car_race) // 2

first_car_time = 0
second_car_time = 0

for first_time in range(len(car_race)):
    if first_time == finish:
        break
    elif car_race[first_time] == 0:
        first_car_time *= 0.80
    else:
        first_car_time += car_race[first_time]
iterate = 0
for second_time in car_race[::-1]:
    iterate += 1
    if second_time == 0:
        second_car_time *= 0.80
    else:
        second_car_time += second_time
    if iterate == finish:
        break

if first_car_time < second_car_time:
    print(f"The winner is left with total time: {first_car_time:.1f}")
else:
    print(f"The winner is right with total time: {second_car_time:.1f}")
