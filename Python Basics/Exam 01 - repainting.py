nylon_price_per_meter = 1.50
paint_price_per_liter = 14.50
thinner_for_paint_per_liter = 5.00

nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_for_masters = int(input())

nylon_needed = nylon_price_per_meter * (nylon_needed + 2)

paint_needed = paint_price_per_liter * (paint_needed + (paint_needed * 0.10))

thinner_needed = thinner_for_paint_per_liter * thinner_needed

total_expenses = nylon_needed + paint_needed + thinner_needed + 0.40

masters_fee = (total_expenses * 0.30) * hours_for_masters
Final_expenses = total_expenses + masters_fee
print(f'Total expenses: {Final_expenses:.2f} lv.')