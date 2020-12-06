n = int(input())
bus_price_per_ton = 200
truck_price_per_ton = 175
train_price_per_ton = 120
total_tons = 0
total_bus = 0
total_truck = 0
total_train = 0

for i in range(1, n + 1):
    tons = int(input())

    if tons <= 3:
        total_bus += tons
    elif 4 <= tons <= 11:
        total_truck += tons
    elif tons >= 12:
        total_train += tons

    total_tons += tons

total_bus_price = total_bus * bus_price_per_ton
total_truck_price = total_truck * truck_price_per_ton
total_train_price = total_train * train_price_per_ton
total_bus_perc = (total_bus / total_tons) * 100
total_truck_perc = (total_truck / total_tons) * 100
total_train_perc = (total_train / total_tons) * 100

average_price_per_ton = (total_bus_price + total_truck_price + total_train_price) / total_tons

print(f'{average_price_per_ton:.2f}')
print(f'{total_bus_perc:.2f}%')
print(f'{total_truck_perc:.2f}%')
print(f'{total_train_perc:.2f}%')