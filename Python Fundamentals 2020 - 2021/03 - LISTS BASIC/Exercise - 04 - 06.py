import sys
numbers = input().split()

n = int(input())

min_num = sys.maxsize
count = 0

while count < n:
    for i in numbers:
        i = int(i)
        if i < min_num:
            min_num = i
    numbers.remove(str(min_num))
    count += 1
    min_num = sys.maxsize


for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(numbers)