# Variant 1

f = open('numbers.txt.txt')
total = 0
for line in f:
    n = int(line.strip())
    total += n

print(total)

f.close()

# VARIANT 2
#
# print(sum([int(line.strip()) for line in open('numbers.txt')]))

# Variant 3
#
# with open('numbers.txt') as numbers:
#     total = 0
#     for n in numbers.readlines():
#         line = int(n.strip())
#         total += line
#     print(total)
