movie_name = input()
package = input()
tickets_number = int(input())
ticket_price = 0

if movie_name == 'John Wick':
    if package == 'Drink':
        ticket_price = 12
    elif package == 'Popcorn':
        ticket_price = 15
    elif package == 'Menu':
        ticket_price = 19
elif movie_name == 'Star Wars':
    if package == 'Drink':
        ticket_price = 18
    elif package == 'Popcorn':
        ticket_price = 25
    elif package == 'Menu':
        ticket_price = 30

elif movie_name == 'Jumanji':
    if package == 'Drink':
        ticket_price = 9
    elif package == 'Popcorn':
        ticket_price = 11
    elif package == 'Menu':
        ticket_price = 14

total_bill = tickets_number * ticket_price

if movie_name == 'Star Wars' and tickets_number >= 4:
    total_bill = total_bill * 0.70
if movie_name == 'Jumanji' and tickets_number == 2:
    total_bill = total_bill * 0.85

print(f'Your bill is {total_bill:.2f} leva.')
