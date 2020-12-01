import math
days_number = int(input())
left_food_kg = int(input())
dog_food_perday = float(input())
cat_food_perday = float(input())
turtle_food_perday = float(input())

dog_food_eaten = dog_food_perday * days_number
cat_food_eten = cat_food_perday * days_number
turtle_food_eaten = (turtle_food_perday * days_number) / 1000
total_food_eaten = dog_food_eaten + cat_food_eten + turtle_food_eaten


if total_food_eaten <= left_food_kg:
    print(f'{math.floor(left_food_kg - total_food_eaten)} kilos of food left.')
else:
    print(f'{math.ceil(total_food_eaten - left_food_kg)} more kilos of food are needed.')