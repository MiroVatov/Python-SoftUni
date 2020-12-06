number_of_easterbreads = int(input())
max_points = 0
top_shef = ''
for i in range(1, number_of_easterbreads + 1):
    baker_name = input()
    grade = input()
    total_points = 0
    while grade != 'Stop':
        grade = int(grade)
        total_points += grade
        grade = input()
    print(f'{baker_name} has {total_points} points.')
    if total_points > max_points:
        max_points = total_points
        top_shef = baker_name
        print(f'{baker_name} is the new number 1!')

print(f'{top_shef} won competition with {max_points} points!')
