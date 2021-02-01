num = int(input())

evens_set = set()
odds_set = set()

for line in range(1, num + 1):
    name = sum(map(ord, input()))
    name = name // line
    if name % 2 == 0:
        evens_set.add(name)
    else:
        odds_set.add(name)

sum_evens = sum(evens_set)
sum_odds = sum(odds_set)

if sum_evens == sum_odds:
    list_output = list(map(str, evens_set | odds_set))
    print(', '.join(list_output))
elif sum_odds > sum_evens:
    list_output = list(map(str, odds_set - evens_set))
    print(', '.join(list_output))
elif sum_evens > sum_odds:
    list_output = list(map(str, odds_set ^ evens_set))
    print(', '.join(list_output))

