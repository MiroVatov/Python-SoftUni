divisor = int(input())
bound = int(input())
max_num = -1_000_000
for index in range(divisor, bound + 1):
    if index % divisor == 0 and bound >= index > 0:
        if index >= max_num:
            max_num = index
print(max_num)
