vegetables_price = float(input())
fruits_price = float(input())
vegatables_qty = int(input())
fruits_qty = int(input())
euro = 1.94

vegatables_income = vegatables_qty * vegetables_price
fruits_income = fruits_qty * fruits_price
Total_income = (vegatables_income + fruits_income) / euro

print(Total_income)

print(vegatables_income)
print(fruits_income)