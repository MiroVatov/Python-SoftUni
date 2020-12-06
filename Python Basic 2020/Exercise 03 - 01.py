projection = input()
rows = int(input())
columns = int(input())

Premiere = 12
Normal = 7.50
Discount = 5

if projection == 'Premiere':
    Premiere = Premiere * rows * columns
    print(f'{Premiere:.2f}')
elif projection == 'Normal':
    Normal = Normal * rows * columns
    print(f'{Normal:.2f}')
elif projection == 'Discount':
    Discount = Discount * rows * columns
    print(f'{Discount:.2f}')


