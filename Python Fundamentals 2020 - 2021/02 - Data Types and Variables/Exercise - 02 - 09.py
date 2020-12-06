import sys
number_of_snowballs = int(input())
max_num = -sys.maxsize
max_snow = 0
max_time = 0
max_quality = 0


for i in range(1, number_of_snowballs + 1):
    snowball_value = 0
    snowball_snow = 0
    snowball_time = 0
    snowball_quality = 0

    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** (snowball_quality)
    if snowball_value >= max_num:
        max_num = snowball_value
        max_snow = snowball_snow
        max_time = snowball_time
        max_quality = snowball_quality

print(f'{max_snow} : {max_time} = {int(max_num)} ({max_quality})')
