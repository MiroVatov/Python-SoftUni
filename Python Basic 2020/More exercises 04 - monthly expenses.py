months = int(input())
water_bill = 20
internet_bill = 15
total_electricity_bill = 0
total_water_bill = 0
total_internet_bill = 0
others = 0
for i in range(1, months + 1):
    electricity_bill = float(input())

    total_electricity_bill += electricity_bill
    total_water_bill += water_bill
    total_internet_bill += internet_bill

    others = total_electricity_bill + total_water_bill + total_internet_bill
total_others = others + (others * 0.20)
avg_per_month = (total_electricity_bill + total_water_bill +total_internet_bill + total_others) / months

print(f'Electricity: {total_electricity_bill:.2f} lv')
print(f'Water: {total_water_bill:.2f} lv')
print(f'Internet: {total_internet_bill:.2f} lv')
print(f'Other: {total_others:.2f} lv')
print(f'Average: {avg_per_month:.2f} lv')

