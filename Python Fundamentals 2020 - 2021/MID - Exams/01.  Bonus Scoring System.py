import math
import sys

students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())

total_bonus = 0

max_bonus = -sys.maxsize
max_attendance = 0

if lectures_count == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for i in range(students_count):

        attendance = int(input())
        total_bonus = (attendance / lectures_count) * (5 + initial_bonus)

        if total_bonus > max_bonus:
            max_bonus = total_bonus
            max_attendance = attendance

    print(f"Max Bonus: {math.ceil(max_bonus)}.")
    print(f"The student has attended {max_attendance} lectures.")




