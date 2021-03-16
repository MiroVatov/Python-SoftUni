from collections import deque

main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']

initial_colors = deque(input().split())

middle = (len(initial_colors) // 2) - 1
collected_main_colors = []

while initial_colors:
    first_part = ''
    second_part = ''

    if initial_colors:
        first_part = initial_colors.popleft()
    if initial_colors:
        second_part = initial_colors.pop()

    if first_part + second_part in main_colors:
        color = first_part + second_part
        collected_main_colors.append(color)

    elif second_part + first_part in main_colors:
        color = second_part + first_part
        collected_main_colors.append(color)

    elif first_part + second_part in secondary_colors:
        color = first_part + second_part
        collected_main_colors.append(color)

    elif second_part + first_part in secondary_colors:
        color = second_part + first_part
        collected_main_colors.append(color)
    else:

        first_part = first_part[:-1]
        second_part = second_part[:-1]
        if first_part:
            initial_colors.insert(middle, first_part)
        if second_part:
            initial_colors.insert(middle, second_part)

for color in collected_main_colors:
    if color == 'orange':
        if 'red' not in collected_main_colors or 'yellow' not in collected_main_colors:
            collected_main_colors.remove(color)
    elif color == 'purple':
        if 'red' not in collected_main_colors or 'blue' not in collected_main_colors:
            collected_main_colors.remove(color)
    elif color == 'green':
        if 'yellow' not in collected_main_colors or 'blue' not in collected_main_colors:
            collected_main_colors.remove(color)

print(collected_main_colors)
