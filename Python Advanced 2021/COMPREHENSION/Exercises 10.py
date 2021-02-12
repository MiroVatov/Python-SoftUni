n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

while True:
    command = input()
    if command == 'END':
        break
    token = command.split()
    action = token[0]
    row = int(token[1])
    col = int(token[2])
    value = int(token[3])
    if action == "Add":
        if 0 <= row < n and 0 <= col < n:
            matrix[row][col] += value
        else:
            print(f"Invalid coordinates")
    elif action == "Subtract":
        if 0 <= row < n and 0 <= col < n:
            matrix[row][col] -= value
        else:
            print(f"Invalid coordinates")
[print(' '.join([str(i) for i in row])) for row in matrix]