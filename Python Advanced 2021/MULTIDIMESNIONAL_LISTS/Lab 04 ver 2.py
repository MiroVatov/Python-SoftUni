def find_searched_symbol(mtrix, search):
    for i, row in enumerate(mtrix):
        for j, value in enumerate(row):
            if search in value:
                index = value.index(search)
                return i, index


n = int(input())
matrix = [list(map(str, input().split())) for _ in range(n)]
searched_symbol = input()

if find_searched_symbol(matrix, searched_symbol):
    res = find_searched_symbol(matrix, searched_symbol)
    print(f'{res}')
else:
    print(f'{searched_symbol} does not occur in the matrix')