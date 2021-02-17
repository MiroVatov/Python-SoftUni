import itertools

rows, cols = [int(el) for el in input().split(', ')]
matrix = [[int(e) for e in input().split(', ')] for row in range(rows)]
max_square = []
squares = []
max_sum = -1_000_000
for i in range(0, rows - 1):
    for j in range(0, cols - 1):
        sq1 = []
        sq2 = []
        sq1.append(matrix[i][j])
        sq1.append(matrix[i][j + 1])
        sq2.append(matrix[i + 1][j])
        sq2.append(matrix[i + 1][j + 1])
        squares.append(sq1)
        squares.append(sq2)
        sum_squares = sum(itertools.chain(*squares))
        if sum_squares > max_sum:
            max_sum = sum_squares
            max_square = squares
        squares = []
for k in max_square:
    a, b = k
    print(a, b)
print(max_sum)