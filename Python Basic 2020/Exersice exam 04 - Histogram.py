n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, n + 1):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number <= 399:
        p2 += 1
    elif 400 <= number <= 599:
        p3 += 1
    elif 600 <= number <= 799:
        p4 += 1
    elif number >= 800:
        p5 += 1

p1 = (p1 / n) * 100
p2 = (p2 / n) * 100
p3 = (p3 / n) * 100
p4 = (p4 / n) * 100
p5 = (p5 / n) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')