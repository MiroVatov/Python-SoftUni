number_of_cargos = int(input())

bus_cargo = 0
truck_cargo = 0
train_cargo = 0
total_cargo = 0
total_price = 0
bus_price = 200
truck_price = 175
train_price = 120

for i in range(1, number_of_cargos + 1):

    current_cargo = int(input())

    if current_cargo <= 3:
        bus_cargo += current_cargo

    elif 4 <= current_cargo <= 11:

        truck_cargo += current_cargo

    elif current_cargo >= 12:
        train_cargo += current_cargo

    total_cargo += current_cargo
final_price = (bus_price * bus_cargo) + (truck_price * truck_cargo) + (train_price * train_cargo)
avg_total_price = final_price / total_cargo
avg_bus_tons = (bus_cargo / total_cargo) * 100
avg_truck_tons = (truck_cargo / total_cargo) * 100
avg_train_tons = (train_cargo / total_cargo) * 100

print(f'{avg_total_price:.2f}')
print(f'{avg_bus_tons:.2f}%')
print(f'{avg_truck_tons:.2f}%')
print(f'{avg_train_tons:.2f}%')