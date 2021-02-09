# numbers = [int(n) for n in input().split(', ')]
# #
# positive = [n for n in numbers if n >= 0]
# negative = [n for n in numbers if n < 0]
# even = [n for n in numbers if n % 2 == 0]
# odd = [n for n in numbers if n % 2 != 0]
#
# print(f"Positive: {', '.join(map(str, positive))}")
# print(f"Negative: {', '.join(map(str, negative))}")
# print(f"Even: {', '.join(map(str, even))}")
# print(f"Odd: {', '.join(map(str, odd))}")

# OR ------- >
# Version 2 -> Shorter ------
numbers = [int(n) for n in input().split(', ')]
print('Positive:', end=' ')
print(', '.join(map(str, [n for n in numbers if n >= 0])))
print('Negative:', end=' ')
print(', '.join(map(str, [n for n in numbers if n < 0])))
print('Even:', end=' ')
print(', '.join(map(str, [n for n in numbers if n % 2 == 0])))
print('Odd:', end=' ')
print(', '.join(map(str, [n for n in numbers if n % 2 != 0])))