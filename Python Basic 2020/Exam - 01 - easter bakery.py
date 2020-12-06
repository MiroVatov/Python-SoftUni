flour_price_per_kg = float(input())
flour_quantity = float(input())
sugar_quantity = float(input())
eggsshells_quantity = int(input())
yeast_qty = int(input())

sugar_price_per_kg = flour_price_per_kg * 0.75
eggshell_price = flour_price_per_kg * 1.10
yeast_price = sugar_price_per_kg * 0.20

total_flour = flour_quantity * flour_price_per_kg
total_sugar = sugar_quantity * sugar_price_per_kg
total_eggshells = eggshell_price * eggsshells_quantity
total_yeast = yeast_qty * yeast_price

Total_bill = total_flour + total_sugar + total_eggshells + total_yeast

print(f'{Total_bill:.2f}')