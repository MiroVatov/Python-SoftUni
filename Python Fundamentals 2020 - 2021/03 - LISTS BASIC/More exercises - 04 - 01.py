numbers = input().split(", ")

for i in numbers:
    if int(i) == 0:

        numbers.append(i[::-1])
        numbers.remove(i)
numbers = [int(n) for n in numbers]

print(numbers)