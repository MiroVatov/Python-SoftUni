from collections import deque
rows, cols = [int(el) for el in input().split()]

matrix = [[''] * cols for _ in range(rows)]

text = deque(input())

for row in range(rows):
    current_text = []
    for col in range(cols):
        current_col = col
        current_char = text.popleft()
        if row % 2 != 0:
            current_col = cols - 1 - col
        matrix[row][current_col] = current_char
        text.append(current_char)
    current_text.append(matrix[row])
    print(''.join([''.join(map(str, row)) for row in current_text]))

