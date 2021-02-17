n = int(input())

matrix = [[e for e in input()] for _ in range(n)]

searched_symbol = input()

found = False

for i in range(len(matrix)):
    for j in range(n):
        if matrix[i][j] == searched_symbol:
            print(f'({i}, {j})')
            found = True
            break
    if found:
        break

if not found:
    print(f'{searched_symbol} does not occur in the matrix')