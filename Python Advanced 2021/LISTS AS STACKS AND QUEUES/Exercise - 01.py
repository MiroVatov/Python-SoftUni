numbers = input().split()

reversed_text = []

while numbers:
    # pop_chart = numbers.pop()
    reversed_text.append(numbers.pop())

print(' '.join(reversed_text))