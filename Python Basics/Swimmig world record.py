import math
record_to_beat = float(input()) # record in seconds
distance_to_cover = float(input()) # Distance in meters
distance_per_meter = float(input()) # distance swimmed per 1 meter
# every 15 meters will be slowed with 12.5 seconds

time_in_seconds = distance_to_cover * distance_per_meter

added_slower_time = math.floor(distance_to_cover / 15)
added_slower_time = added_slower_time * 12.5

total_swim_time = time_in_seconds + added_slower_time

if_isnot_record = total_swim_time - record_to_beat
if total_swim_time < record_to_beat:
    print(f'Yes, he succeeded! The new world record is {total_swim_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {if_isnot_record:.2f} seconds slower.')