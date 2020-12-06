days_of_vacation = int(input())
budget = float(input())
number_of_people = int(input())
price_per_km = float(input())
food_per_person_per_day = float(input())
hotel_room_per_person_per_night = float(input())

food_expenses = (days_of_vacation * number_of_people * food_per_person_per_day)
hotel_all_nights_price = (days_of_vacation * hotel_room_per_person_per_night * number_of_people)
success_trip = True
consumed_fuel = 0

if number_of_people > 10:
    hotel_all_nights_price = hotel_all_nights_price * 0.75

total_expenses = food_expenses + hotel_all_nights_price

for day in range(1, days_of_vacation + 1):
    km_per_day = float(input())
    consumed_fuel = (price_per_km * km_per_day)
    total_expenses += consumed_fuel

    if day % 3 == 0 or day % 5 == 0:
        additional_expenses = total_expenses * 0.40
        total_expenses += additional_expenses
    if day % 7 == 0:
        received_amount = total_expenses / number_of_people
        total_expenses -= received_amount

    if total_expenses > budget:
        diff = total_expenses - budget
        success_trip = False
        print(f"Not enough money to continue the trip. You need {diff:.2f}$ more.")
        break

if success_trip:
    diff = budget - total_expenses
    print(f"You have reached the destination. You have {diff:.2f}$ budget left.")



