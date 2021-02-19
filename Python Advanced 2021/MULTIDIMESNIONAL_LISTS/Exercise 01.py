n = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

sum_primary_diagonal = 0

for i in range(len(matrix)):
    value = matrix[i][i]
    sum_primary_diagonal += value

sum_secondary_diagonal = 0
for j in range(len(matrix)):
    value = matrix[j][n-j-1]
    sum_secondary_diagonal += value
diff = abs(sum_primary_diagonal - sum_secondary_diagonal)
print(diff)