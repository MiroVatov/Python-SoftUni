import math
vineyard_area = int(input())
grape_per_sqrmeter = float(input())
wine_liters_needed = int(input())
workers = int(input())

total_grape = vineyard_area * grape_per_sqrmeter
wine_produced = (total_grape * 0.40) / 2.5

wine_per_person = (wine_produced - wine_liters_needed) / workers

if wine_produced < wine_liters_needed:
    wine_needed = wine_liters_needed - wine_produced
    print(f'It will be a tough winter! More {math.floor(wine_needed)} liters wine needed.')
else:
    wine_left = wine_produced - wine_liters_needed
    print(f'Good harvest this year! Total wine: {math.floor(wine_produced)} liters.')
    print(f'{math.ceil(wine_left)} liters left -> {math.ceil(wine_per_person)} liters per person.')