number = int(input())
bonus_points = 0

if number <= 100:
    bonus_points = 5
elif 100 < number <= 1000:
    bonus_points = 0.2 * number
elif number > 1000:
    bonus_points = 0.1 * number

if number % 2 == 0:
    bonus_points = bonus_points + 1
elif number % 10 == 5:
    bonus_points = bonus_points + 2

number = number + bonus_points

print(bonus_points)
print(number)