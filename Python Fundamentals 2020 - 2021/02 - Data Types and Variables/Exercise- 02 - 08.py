import math
companions = int(input())
days = int(input())

total_coins = 0


for day in range(1, days + 1):
    motivational_party = False
    if day % 15 == 0:
        companions += 5

    if day % 10 == 0:
        companions -= 2

    total_coins += 50 - (companions * 2)

    if day % 3 == 0:
        total_coins -= (companions * 3)
        motivational_party = True
    if day % 5 == 0:
        total_coins += (companions * 20)
        if motivational_party:
            total_coins -= (companions * 2)


total_coins = math.floor(total_coins / companions)

print(f'{companions} companions received {total_coins} coins each.')