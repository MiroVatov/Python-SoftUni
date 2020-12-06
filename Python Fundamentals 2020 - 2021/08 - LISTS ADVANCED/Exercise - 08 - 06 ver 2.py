import math
nums = list(map(int, input().split(', ')))

max_num = max(nums)
number_of_groups = math.ceil(max_num / 10)

for i in range(1, number_of_groups + 1):
    current_range = []

    for num in nums:
        upper_range = i * 10
        lower_range = upper_range - 10
        if lower_range < num <= upper_range:
            current_range.append(num)

    print(f'Group of {i * 10}\'s: {current_range}')

