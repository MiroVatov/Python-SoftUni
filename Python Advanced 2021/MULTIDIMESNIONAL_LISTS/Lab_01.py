import itertools
rows, cols = [int(i) for i in input().split(', ')]
matrix = []
sum_matrix = 0
for i in range(rows):
    elem = [int(el) for el in input().split(', ')]
    matrix.append(elem)
    # Variant 1 ->>>>>
    # sum_matrix += sum([el for el in elem])
sum_matrix = sum(itertools.chain(*matrix))

print(sum_matrix)
print(matrix)
