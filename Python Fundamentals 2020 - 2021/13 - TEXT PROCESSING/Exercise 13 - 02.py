import itertools

initial_string = input().split()

first_string = initial_string[0]
second_string = initial_string[1]

sum_of_string = 0

for (a, b) in itertools.zip_longest(first_string, second_string, fillvalue=' '):
    if a == ' ':
        sum_of_string += (ord(b))
    elif b == ' ':
        sum_of_string += (ord(a))
    else:
        sum_of_string += (ord(a) * ord(b))

print(sum_of_string)

