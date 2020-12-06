total_price_without_taxes = 0

while True:
    command = input()
    if command == "special" or command == "regular":
        break
    price = float(command)
    if price < 0:
        print(f"Invalid price!")
        continue
    total_price_without_taxes += price

Final_price = total_price_without_taxes * 1.20

if Final_price == 0:
    print(f"Invalid order!")
else:
    if command == "special":
        Final_price *= 0.90

    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_price_without_taxes * 0.20:.2f}$")
    print(f"-----------")
    print(f'Total price: {Final_price:.2f}$')

