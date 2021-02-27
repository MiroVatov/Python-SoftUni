from itertools import combinations

people = input().split(', ')
n = int(input())

for comb in combinations(people, n):
    print(', '.join(comb))