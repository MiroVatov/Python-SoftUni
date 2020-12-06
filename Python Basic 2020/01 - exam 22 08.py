processor_price = float(input())
videocard_price = float(input())
ram_price = float(input())
rams_qty = int(input())
percent_discount = float(input())

processor_total = processor_price * 1.57
videcard_total = videocard_price * 1.57
ram_total = (ram_price * 1.57) * rams_qty

processor_total = processor_total - (percent_discount * processor_total)
videcard_total = videcard_total - (percent_discount * videcard_total)

total_bill = processor_total + videcard_total + ram_total

print(f'{total_bill:.2f} leva.')

