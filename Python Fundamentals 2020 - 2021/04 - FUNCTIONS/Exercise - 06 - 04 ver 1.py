number = input()
number = [n for n in number]

def evens_odds():
    evens = 0
    odds = 0

    for i in number :
        if int(i) % 2 == 0:
            evens += int(i)

        else:
            odds += int(i)

    return f'Odd sum = {odds}, Even sum = {evens}'

print(evens_odds())
