num = int(input())

evens_set = set()
odds_set = set()
current_line = 0

for line in range(1, num + 1):
    name = input()
    name_ascii = 0
    for n in name:
        name_ascii += ord(n)
    name_ascii = name_ascii // line
    if name_ascii % 2 == 0:
        evens_set.add(name_ascii)
    else:
        odds_set.add(name_ascii)

sum_evens = sum(evens_set)
sum_odds = sum(odds_set)

result = []

if sum_evens == sum_odds:
    result = odds_set.union(evens_set)
elif sum_odds > sum_evens:
    result = odds_set.difference(evens_set)
elif sum_evens > sum_odds:
    result = odds_set.symmetric_difference(evens_set)

print(', '.join(str(x) for x in result))
