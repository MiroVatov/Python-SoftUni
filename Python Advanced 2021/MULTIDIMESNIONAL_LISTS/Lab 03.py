n = int(input())


# matrix = []
# for _ in range(n):
#     matrix.append([int(e) for e in input().split()])

matrix = [[int(e) for e in input().split()] for _ in range(n)]

sum_primary_diagonal = 0
counter = 0
for i in range(len(matrix)):

    value = matrix[counter][i]
    sum_primary_diagonal += value
    counter += 1
print(sum_primary_diagonal)
