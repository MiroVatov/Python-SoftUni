sizes = list(map(int, input().split(", ")))
columns = sizes[1]
rows = sizes[0]
matrix = [[0] * columns for row in range(rows)]

for row in range(rows):
    lines = list(map(int, input().split()))
    for column in range(columns):
        matrix[row][column] = lines[column]
summed = [0] * columns

for column in range(columns):
    for row in range(rows):
        summed[column] += matrix[row][column]
    print(summed[column])
