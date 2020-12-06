population = input().split(", ")
population = list(map(int, population))
minimum_wealth = int(input())
not_possible = False
max_money_index = 0

for i in range(len(population)):
    diff = abs(population[i] - minimum_wealth)
    max_money = max(population)

    max_money_index = population.index(max_money)
    if population[i] < minimum_wealth:

        if (max_money - diff) >= minimum_wealth:
            population[i] += diff
            population[max_money_index] -= diff
        else:
            print(f"No equal distribution possible")
            not_possible = True
            break
    if not_possible:
        break
if not not_possible:
    print(population)


