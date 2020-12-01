strawberries_price = float(input())
bananas_qty = float(input())
oranges_qty = float(input())
raspberries_qty = float(input())
strawberries_qty = float(input())

raspberries_price = strawberries_price * 0.5
oranges_price = 0.6 * raspberries_price
bananas_price = 0.2 * raspberries_price
sum_of_raspberries = raspberries_qty * raspberries_price
sum_of_oranges = oranges_qty * oranges_price
sum_of_bananas = bananas_qty * bananas_price
sum_of_strawberries = strawberries_qty * strawberries_price

Total_sum = sum_of_bananas + sum_of_oranges + sum_of_raspberries + sum_of_strawberries

print(Total_sum)
