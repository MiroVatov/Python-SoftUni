numbers = input().split(", ")

for i in numbers:
    if int(i) == 0:
        numbers.append(numbers.pop(numbers.index(i)))

numbers = [int(n) for n in numbers]

print(numbers)