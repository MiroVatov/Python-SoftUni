import math
serial_name = input()
seasons_number = int(input())
series_number = int(input())
episode_time = float(input())

total_episode_time = episode_time * 1.20
additional_time_special_episode = seasons_number * 10
total_time = seasons_number * series_number * total_episode_time + additional_time_special_episode
print(f'Total time needed to watch the {serial_name} series is {math.floor(total_time)} minutes.')