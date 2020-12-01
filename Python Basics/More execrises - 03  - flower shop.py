chrysanthemums_bought = int(input())
roses_bought = int(input())
tulips_bought = int(input())
season = input()
holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50

if season == 'Autumn' or season == 'Winter':
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

total_flowers = chrysanthemums_bought + roses_bought + tulips_bought
bouquet_price = (tulips_bought * tulips_price) + (chrysanthemums_bought * chrysanthemums_price) + (roses_bought * roses_price)

if holiday == 'Y':
    bouquet_price *= 1.15
if tulips_bought > 7 and season == 'Spring':
    bouquet_price = bouquet_price * 0.95
if roses_bought >= 10 and season == 'Winter':
    bouquet_price = bouquet_price * 0.90
if total_flowers > 20:
    bouquet_price = bouquet_price * 0.80

print(f'{bouquet_price + 2:.2f}')