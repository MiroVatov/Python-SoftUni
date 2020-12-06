journey_cost = float(input())
months_num = int(input())



total_saving = 0

for m in range(1, months_num + 1):


    if m % 2 != 0 and not m == 1:
        odd_monthly_spendings = total_saving * 0.16
        total_saving -= odd_monthly_spendings
    if m % 4 == 0:
        bonus = total_saving * 0.25
        total_saving += bonus

    total_saving += (journey_cost * 0.25)

if total_saving >= journey_cost:
    diff = total_saving - journey_cost
    print(f"Bravo! You can go to Disneyland and you will have {diff:.2f}lv. for souvenirs.")

else:
    diff = journey_cost - total_saving
    print(f"Sorry. You need {diff:.2f}lv. more.")