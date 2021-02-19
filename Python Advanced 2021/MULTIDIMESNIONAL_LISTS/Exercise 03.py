import itertools
rows, cols = [int(el) for el in input().split()]
matrix = [[int(e) for e in input().split()] for _ in range(rows)]
squares = []
max_square = []
max_sum = -1_000_000
for i in range(len(matrix) - 2):
    row = matrix[i]
    for j in range(len(row) - 2):
        square = [
            [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
            [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
            [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]],
        ]
        squares.append(square)
        sum_squares = sum(itertools.chain(*square))
        if sum_squares > max_sum:
            max_sum = sum_squares
            max_square = squares
        squares = []

print(f'Sum = {max_sum}')
for k in max_square:
    for v in k:
        a, b, c = v
        print(a, b, c)

         