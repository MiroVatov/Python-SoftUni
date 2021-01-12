# raw_input = input().split()
# first_set_length = int(raw_input[0])
# second_set_length = int(raw_input[1])

first_set_length, second_set_length = [int(x) for x in input().split(' ')]

first_set = set()
second_set = set()

for _ in range(first_set_length):
    first_set.add(int(input()))
for _ in range(second_set_length):
    second_set.add(int(input()))

intersect = first_set.intersection(second_set)

for num in intersect:
    print(num)