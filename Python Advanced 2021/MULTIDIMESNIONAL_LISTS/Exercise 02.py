rows, cols = [int(el) for el in input().split()]
matrix = [[e for e in input().split()] for _ in range(rows)]

equal_squares = 0
for i in range(0, rows - 1):
    for j in range(0, cols - 1):
        sq1 = ''
        sq2 = ''
        char1 = matrix[i][j]
        char2 = matrix[i][j + 1]
        char3 = matrix[i + 1][j]
        char4 = matrix[i + 1][j + 1]
        if char1 == char2:
            sq1 = char1 + char2
            if char3 == char4:
                sq2 = char3 + char4
                if sq1 == sq2:
                    equal_squares += 1

print(equal_squares)