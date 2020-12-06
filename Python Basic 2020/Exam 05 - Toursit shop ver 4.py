budget = float(input())

counter = 0
bill = 0

while True:
    product = input()
    if product == "Stop":
        print(f"You bought {counter} products for {bill:.2f} leva.")
        break

    item_price = float(input())

    if (counter + 1) % 3 == 0:
        item_price *= 0.5

    if item_price + bill > budget:
        diff = item_price + bill - budget
        print("You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break

    counter += 1
    bill += item_price