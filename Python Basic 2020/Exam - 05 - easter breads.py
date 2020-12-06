import sys
import math
number_of_breads = int(input())
total_sugar = 0
total_flour = 0
max_sugar = -sys.maxsize
max_fluor = -sys.maxsize

for i in range(1, number_of_breads + 1):
    sugar = int(input())
    fluor = int(input())
    if sugar > max_sugar:
        max_sugar = sugar
    if fluor > max_fluor:
        max_fluor = fluor
    total_sugar += sugar
    total_flour += fluor

sugar_packs = total_sugar / 950
fluor_packs = total_flour / 750

print(f'Sugar: {math.ceil(sugar_packs)}')
print(f'Flour: {math.ceil(fluor_packs)}')
print(f'Max used flour is {max_fluor} grams, max used sugar is {max_sugar} grams.')