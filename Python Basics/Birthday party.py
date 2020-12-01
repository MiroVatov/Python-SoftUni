rent = int(input())

cake = 0.20 * rent
drinks = 0.55 * cake
animator = rent / 3
budget = cake + drinks + animator + rent

print(f'{budget:.2f}')

print(cake)
print(drinks)
print(animator)