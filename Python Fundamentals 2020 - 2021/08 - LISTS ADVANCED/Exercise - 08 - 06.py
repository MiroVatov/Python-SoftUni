numbers_list = input().split(', ')
numbers_list = [int(n) for n in numbers_list]

boundary = 10

while len(numbers_list) > 0:
    new_list = []
    for num in numbers_list:

        if num <= boundary:
            new_list.append(num)

    print(f'Group of {boundary}\'s: {new_list}')

    for i in numbers_list[::-1]:
        if i in new_list:
           numbers_list.remove(i)

    boundary += 10
