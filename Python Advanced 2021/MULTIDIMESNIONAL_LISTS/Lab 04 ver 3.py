def find_searched_symbol(mtrix, search):
    for i, row in enumerate(mtrix):

        for j, value in enumerate(row):
            if value == search:
                return i, j


n = int(input())
matrix = [list(input()) for _ in range(n)]
searched_symbol = input()

res = find_searched_symbol(matrix, searched_symbol)

if res:
    print(f'{res}')
else:
    print(f'{searched_symbol} does not occur in the matrix')