number_of_cars = int(input())

cars_available = {}

for c in range(number_of_cars):
    car_derails = input().split("|")
    car_maker = car_derails[0]
    mileage = int(car_derails[1])
    fuel_available = int(car_derails[2])
    if c not in car_derails:
        cars_available[car_maker] = [mileage, fuel_available]

while True:
    command = input()
    if command == "Stop":
        break

    token = command.split(" : ")
    action = token[0]

    if action == "Drive":
        car = token[1]
        distance = int(token[2])
        fuel = int(token[3])
        if fuel > cars_available[car][1]:
            print(f"Not enough fuel to make that ride")
        else:
            cars_available[car][0] += distance
            cars_available[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_available[car][0] >= 100000:
                del cars_available[car]
                print(f"Time to sell the {car}!")

    elif action == "Refuel":
        car = token[1]
        fuel = int(token[2])
        if fuel + cars_available[car][1] >= 75:
            fuel_used = 75 - cars_available[car][1]
            cars_available[car][1] = 75
            print(f"{car} refueled with {fuel_used} liters")
        else:
            cars_available[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        car = token[1]
        kilometers = int(token[2])
        cars_available[car][0] -= kilometers
        if cars_available[car][0] < 10000:
            cars_available[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")


sorted_cars_dict = dict(sorted(cars_available.items(),key=lambda x: (-x[1][0], x[0])))

for c, value in sorted_cars_dict.items():
    print(f"{c} ->", end=' ')
    for m in value:
        print(f"Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
        break