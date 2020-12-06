pens_price = 5.8
markers_price = 7.2
detergent_per_liter = 1.2

pens_qty = int(input())
markers_qty = int(input())
detergent_liters = float(input())
percent_discount = int(input())

total_bill = (pens_qty * pens_price) + (markers_qty * markers_price) + (detergent_liters * detergent_per_liter)
tital_bill_discounted = total_bill - (total_bill * (percent_discount / 100))
print(f'{tital_bill_discounted:.3f}')