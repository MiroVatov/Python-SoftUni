people_number = int(input())
man_strenght = int(input())
Illidan_blood = int(input())

total_strenght = people_number * man_strenght

if total_strenght < Illidan_blood:
    diff = Illidan_blood - total_strenght
    print(f'You are not prepared! You need {diff} more points.')
elif total_strenght >= Illidan_blood:
    diff = total_strenght - Illidan_blood
    print(f'Illidan has been slain! You defeated him with {diff} points.')