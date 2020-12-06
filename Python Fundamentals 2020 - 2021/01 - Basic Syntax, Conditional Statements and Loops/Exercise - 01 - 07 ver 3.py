divisor = int(input())
bound = int(input())

for index in range(bound, divisor, -1):
    if index % divisor == 0:
        print(index)
        break
