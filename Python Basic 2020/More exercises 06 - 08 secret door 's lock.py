hunderds = int(input())
dozens = int(input())
units = int(input())

for h in range(1, hunderds + 1):
    for d in range (2, dozens + 1):
        for u in range(1, units + 1):
            if (h % 2 == 0 and u % 2 == 0) and (d == 2 or d == 3 or d == 5 or d == 7):
                print(f'{h} {d} {u}')
            else:
                continue