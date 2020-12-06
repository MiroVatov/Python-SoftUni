import math
import sys

max_sugar = -sys.maxsize
max_fluor = -sys.maxsize
breads_qty = int(input())
total_sugar = 0
total_fluor = 0

for i in range(breads_qty):
    sugar_grams = int(input())
    flour_grams = int(input())
    bread = sugar_grams + flour_grams

    if sugar_grams > max_sugar:
        max_sugar = sugar_grams
    if flour_grams > max_fluor:
        max_fluor = flour_grams

    total_sugar += sugar_grams
    total_fluor += flour_grams

sugar_packages = math.ceil(total_sugar / 950)
fluor_packages = math.ceil(total_fluor / 750)

print(f'Sugar: {sugar_packages}')
print(f'Flour: {fluor_packages}')
print(f'Max used flour is {max_fluor} grams, max used sugar is {max_sugar} grams.')