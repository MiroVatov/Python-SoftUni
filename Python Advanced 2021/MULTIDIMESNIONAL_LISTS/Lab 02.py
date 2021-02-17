rows, cols = [int(el) for el in input().split(', ')]
sum_cols = 0

matrix = [[int(e) for e in input().split(' ')] for row in range(rows)]

# Variant 1 ->>>>>>

# for i in range(cols):
#     for j in range(rows):
#         value = matrix[j][i]
#         sum_cols += value
#     print(sum_cols)
#     sum_cols = 0

# Variant 2 ->>>>>>>>>

# for j in range(cols):
#     for row in matrix:
#         sum_cols += row[j]
#     print(sum_cols)
#     sum_cols = 0

# Variant 3 ->>>>>>>>>

for col in zip(*matrix):
    print(sum(col))