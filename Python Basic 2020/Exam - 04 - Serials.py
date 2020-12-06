budget = float(input())
serials_number = int(input())
total_series_price = 0

for i in range(1, serials_number + 1):
    serial_name = input()
    serial_price = float(input())
    if serial_name == 'Thrones':
        serial_price = serial_price * 0.5
    elif serial_name == 'Lucifer':
        serial_price = serial_price * 0.6
    elif serial_name == 'Protector':
        serial_price = serial_price * 0.70
    elif serial_name == 'TotalDrama':
        serial_price = serial_price * 0.80
    elif serial_name == 'Area':
        serial_price = serial_price * 0.90

    total_series_price += serial_price

if budget >= total_series_price:
    diff = budget - total_series_price
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    diff = total_series_price - budget
    print(f'You need {diff:.2f} lv. more to buy the series!')