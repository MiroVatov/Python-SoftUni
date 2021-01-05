# numbers_input = input().split()
#
# numbers_dict = {}
#
# for i in range(len(numbers_input)):
#     number = numbers_input[i]
#     if number not in numbers_dict:
#         numbers_dict[number] = []
#     numbers_dict[number].append(number)
#
# for num, count in numbers_dict.items():
#     print(f"{float(num)} - {len(count)} times")


# VERSION 2 FROM THE PRESENTATION

numbers = tuple(map(float, input().split()))

numb_dict = {}
for num in numbers:
    if num not in numb_dict:
        numb_dict[num] = 0
    numb_dict[num] += 1
[print(f"{key} - {value} times") for key, value in numb_dict.items()]
