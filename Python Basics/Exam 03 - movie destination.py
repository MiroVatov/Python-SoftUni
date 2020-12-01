movie_budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

shooting_day_cost = 0
total_movie_cost = 0

if destination == 'Dubai':
    if season == 'Winter':
        shooting_day_cost = 45000
    elif season == 'Summer':
        shooting_day_cost = 40000
elif destination == 'Sofia':
    if season == 'Winter':
        shooting_day_cost = 17000
    elif season == 'Summer':
        shooting_day_cost = 12500
elif destination == 'London':
    if season == 'Winter':
        shooting_day_cost = 24000
    elif season == 'Summer':
        shooting_day_cost = 20250

total_movie_cost = number_of_days * shooting_day_cost

if destination == 'Dubai':
    total_movie_cost = total_movie_cost * 0.70
if destination == 'Sofia':
    total_movie_cost = total_movie_cost * 1.25

if movie_budget >= total_movie_cost:
    diff = movie_budget - total_movie_cost
    print(f'The budget for the movie is enough! We have {diff:.2f} leva left!')
else:
    diff = total_movie_cost - movie_budget
    print(f'The director needs {diff:.2f} leva more!')