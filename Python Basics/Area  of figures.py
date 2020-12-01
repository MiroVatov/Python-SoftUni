import math
figure = input()
area = 0

if figure == 'square':
    side = float(input())
    area = side ** 2
elif figure == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2
elif figure == 'circle':
    radius = float(input())
    area = math.pi * (radius ** 2)
elif figure == 'triangle':
    side1 = float(input())
    side2 = float(input())
    area = (side1 * side2) / 2

print(f'{area:.3f}')
