n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

total = 0

for i in range(n):
    value = matrix[i][i]
    total += value

print(total)
