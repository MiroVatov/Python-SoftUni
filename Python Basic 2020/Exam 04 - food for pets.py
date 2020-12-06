days = int(input())
total_food = float(input())
total_dog_eaten = 0
total_cat_eaten = 0
total_biscuits = 0
for i in range(1, days + 1):
    dog_eats = int(input())
    cat_eats = int(input())
    biscuits = 0.0
    total_dog_eaten += dog_eats
    total_cat_eaten += cat_eats
    total_pet_food_per_day = cat_eats + dog_eats
    if i % 3 == 0:
        biscuits = total_pet_food_per_day * 0.10
    total_biscuits += biscuits

total_food_eaten = total_dog_eaten + total_cat_eaten
perc_dog_eaten = (total_dog_eaten / total_food_eaten) * 100
perc_cat_eaten = (total_cat_eaten / total_food_eaten) * 100
perc_food_eaten = (total_food_eaten / total_food) * 100
print(f'Total eaten biscuits: {round(total_biscuits)}gr.')
print(f'{perc_food_eaten:.2f}% of the food has been eaten.')
print(f'{perc_dog_eaten:.2f}% eaten from the dog.')
print(f'{perc_cat_eaten:.2f}% eaten from the cat.')