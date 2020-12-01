import math
serial_name = input()
serial_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
free_time = break_time * 0.25

left_time = break_time - lunch_time - free_time

if left_time >= serial_time:
    diff = left_time - serial_time
    print(f'You have enough time to watch {serial_name} and left with {math.ceil(diff)} minutes free time.')
else:
    diff = serial_time - left_time
    print(f'You don\'t have enough time to watch {serial_name}, you need {math.ceil(diff)} more minutes.')