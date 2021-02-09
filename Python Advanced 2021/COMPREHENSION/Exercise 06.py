rows, cols = [int(el) for el in input.split()]

matrix = [[f"{chr(row)}{chr(row + col)}{chr(row)}" for col in range(cols)] for row in range(97, 97 + rows)]

[print(' '.join([col for col in row])) for row in matrix]