number_of_days = int(input())
count_of_players = int(input())
groups_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())

water_needed = number_of_days * count_of_players * water_per_day_per_person
food_needed = number_of_days * count_of_players * food_per_day_per_person

success = True

for day in range(1, number_of_days + 1):
    energy_loss = float(input())
    groups_energy -= energy_loss

    if groups_energy <= 0:
        success = False
        break
    if day % 2 == 0:
        energy_boost = groups_energy * 0.05
        groups_energy += energy_boost
        drop_water = water_needed * 0.30
        water_needed -= drop_water

    if day % 3 == 0:
        drop_food = food_needed / count_of_players
        food_needed -= drop_food
        groups_energy += groups_energy * 0.10

if success:
    print(f"You are ready for the quest. You will be left with - {groups_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food_needed:.2f} food and {water_needed:.2f} water.")
