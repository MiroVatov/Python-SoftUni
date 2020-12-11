def drive(cars, car, dist, fuel):
    if fuel > cars[car][1]:
        print(f"Not enough fuel to make that ride")

    else:
        cars[car][0] += dist
        cars[car][1] -= fuel
        print(f"{car} driven for {dist} kilometers. {fuel} liters of fuel consumed.")
        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    return cars


def refuel(cars, car, fuel):
    if fuel + cars[car][1] >= 75:
        fuel_used = 75 - cars[car][1]
        cars[car][1] = 75
        print(f"{car} refueled with {fuel_used} liters")
    else:
        cars[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")
    return cars


def revert(cars, c, km):
    cars[c][0] -= km
    if cars[c][0] < 10000:
        cars[c][0] = 10000
    else:
        print(f"{c} mileage decreased by {km} kilometers")
    return cars


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
        cars_available = drive(cars_available, car, distance, fuel)

    elif action == "Refuel":
        car = token[1]
        fuel = int(token[2])
        cars_available = refuel(cars_available, car, fuel)

    elif action == "Revert":
        car = token[1]
        kilometers = int(token[2])
        cars_available = revert(cars_available, car, kilometers)


sorted_cars_dict = dict(sorted(cars_available.items(),key=lambda x: (-x[1][0], x[0]))) 

for c, value in sorted_cars_dict.items():
    print(f"{c} ->", end=' ')
    for m in value:
        print(f"Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
        break