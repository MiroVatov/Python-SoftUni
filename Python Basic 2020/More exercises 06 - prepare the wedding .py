men = int(input())
women = int(input())
tables_max = int(input())
tables = 0
for m in range(1, men + 1):
    for w in range(1, women + 1):
        print(f'({m} <-> {w})', end=' ')

        tables += 1
        if tables == tables_max:
            break

    if tables == tables_max:
        break