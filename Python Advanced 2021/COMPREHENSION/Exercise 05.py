matrix = [[i for i in input().split(', ')] for _ in range(int(input()))]

first_diagonal = [matrix[i][i] for i in range(len(matrix))]

print(f"First diagonal: {', '.join(first_diagonal)}. Sum: {sum(map(int, first_diagonal))}")

second_diagonal = [matrix[len(matrix)-1 - i][i] for i in range(len(matrix) - 1, -1, -1)]

print(f"Second diagonal: {', '.join(second_diagonal)}. Sum: {sum(map(int, second_diagonal))}")