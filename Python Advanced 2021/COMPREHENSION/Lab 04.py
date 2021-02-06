matrix = [[int(n) for n in input().split(', ')] for i in range(int(input()))]
flat_matrix = [num for row in matrix for num in row]
print(flat_matrix)