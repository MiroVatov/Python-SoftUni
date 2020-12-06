total_people = int(input())
strenght = int(input())
Ildan_blood = int(input())

total_strenght = total_people * strenght

diff = abs(Ildan_blood - total_strenght)
if total_strenght < Ildan_blood:

    print(f'You are not prepared! You need {diff} more points.')
else:
    print(f'Illidan has been slain! You defeated him with {diff} points.')