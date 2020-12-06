k = int(input())
l = int(input())
m = int(input())
n = int(input())
substitutes_count = 0
for a in range(k, 9):
    for b in range(9, l - 1, -1):

        for c in range(m, 9):
            for d in range(9, n - 1, -1):
                first_number = str(a) + str(b)
                second_number = str(c) + str(d)
                if (a % 2 == 0 and c % 2 == 0) and (b % 2 != 0 and d % 2 != 0):
                    if first_number != second_number:
                        substitutes_count += 1
                        print(f'{str(a)}{str(b)} - {str(c)}{str(d)}')
                        if substitutes_count == 6:
                            break
                    else:
                        print(f'Cannot change the same player.')
    if substitutes_count == 6:
        break