time_to_beat_in_minutes = int(input())
time_to_beat_in_seconds = int(input())
track_length = float(input())
seconds_for_100_meters = int(input())

complete_time_to_beat_in_seconds = (time_to_beat_in_minutes * 60) + time_to_beat_in_seconds
slowed_time = track_length / 120
total_slowed_time = slowed_time * 2.5

race_time = (track_length / 100) * seconds_for_100_meters - total_slowed_time

difference = abs(race_time - complete_time_to_beat_in_seconds)

if race_time <= complete_time_to_beat_in_seconds:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {race_time:.3f}.')
else:
    print(f'No, Marin failed! He was {difference:.3f} second slower.')