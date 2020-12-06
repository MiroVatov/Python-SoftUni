cinema_capacity = int(input())
ticket_price = 5
total_income = 0
#free_places = 0
people = input()
full = False
while people != 'Movie time!':
    people = int(people)
    if people > cinema_capacity:
        full = True
        break
    if people % 3 == 0:
        current_income = (people * ticket_price) - 5
        cinema_capacity -= people
    else:
        current_income = people * ticket_price
        cinema_capacity -= people

    total_income += current_income
    people = input()

if full == False:
    print(f'There are {cinema_capacity} seats left in the cinema.')
if full == True:
    print(f'The cinema is full.')

print(f'Cinema income - {total_income} lv.')