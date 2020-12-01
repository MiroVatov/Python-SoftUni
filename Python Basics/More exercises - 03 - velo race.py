number_of_juniors = int(input())
number_of_seniors = int(input())
type_of_race = input()

juniors_fee = 0
seniors_fee = 0
sum_donated = 0
total_fee = 0

if type_of_race == 'trail':
    juniors_fee = 5.50
    seniors_fee = 7
elif type_of_race == 'cross-country':
    juniors_fee = 8
    seniors_fee = 9.50
elif type_of_race == 'downhill':
    juniors_fee = 12.25
    seniors_fee = 13.75
elif type_of_race == 'road':
    juniors_fee = 20
    seniors_fee = 21.50

total_participants = number_of_juniors + number_of_seniors
total_fee = ((juniors_fee * number_of_juniors) + (seniors_fee * number_of_seniors)) * 0.95

if type_of_race == 'cross-country' and total_participants >= 50:
    total_fee = total_fee * 0.75

print(f'{total_fee:.2f}')