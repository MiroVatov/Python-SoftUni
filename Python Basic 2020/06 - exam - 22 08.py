k = int(input())
l = int(input())
m = int(input())
n = int(input())

substitutes = 0

for a in range(k, 9):
    for b in range(9 , l - 1, -1):
        for c in range(m, 9):
            for d in range(9 , n - 1, -1):
                if a % 2 == 0 and c % 2 == 0 and b % 2 != 0 and d % 2 != 0:

                    if str(a) + str(b) == str(c) + str(d):
                        print(f'Cannot change the same player.')
                    else:
                        print(f'{a}{b} - {c}{d}')
                        substitutes += 1
                        if substitutes == 6:
                            break
            if substitutes == 6:
                break
        if substitutes == 6:
            break
    if substitutes == 6:
        break