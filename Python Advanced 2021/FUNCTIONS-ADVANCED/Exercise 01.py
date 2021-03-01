# print([int(i) for i in input().split() if int(i) % 2 == 0])

numbers = list(map(int, input().split()))

print(list(filter(lambda x: x % 2 == 0, numbers)))
