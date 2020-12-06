divisor = int(input())
bound = int(input())
max_count = 0
for index in range(divisor, bound + 1):
    if index % divisor == 0 and bound >= index > 0:
        max_count = index
print(max_count)
