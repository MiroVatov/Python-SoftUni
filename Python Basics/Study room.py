import math
length = float(input()) * 100
width = float(input()) * 100
lines = math.trunc(length / 120)
columns = math.trunc(width / 70) - 1
seats = (lines * columns) - 3

print(seats)

print(lines)
print(columns)

'''

length = float(input()) * 100
width = float(input()) * 100
lines = (length // 120)
columns = (width // 70) - 1
seats = (lines * columns) - 3

print(int(seats))

'''