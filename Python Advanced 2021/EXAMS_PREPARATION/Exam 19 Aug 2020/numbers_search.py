def numbers_searching(*args):
    duplicates = set()
    missing = 0
    nums_list = args
    for num in nums_list:
        if nums_list.count(num) > 1:
            duplicates.add(num)
    numbers_in_range = list(range(min(nums_list), max(nums_list)+1))
    for number in numbers_in_range:
        if number not in nums_list:
            missing = number
    return [missing, sorted(duplicates)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
