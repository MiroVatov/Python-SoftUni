days_of_campaign = int(input())
cookers = int(input())
cakes = int(input())
gofretas = int(input())
pancakes = int(input())

cake_price = 45
gofreta_price = 5.80
pancake_price = 3.20

cakes = cakes * cake_price
gofretas = gofretas * gofreta_price
pancakes = pancakes * pancake_price
daily_sum = (cakes + gofretas + pancakes) * cookers
Sum_for_campaign = daily_sum * days_of_campaign
Sum_for_the_expenses = Sum_for_campaign - (Sum_for_campaign / 8)

print(f'{Sum_for_the_expenses:.2f}')



