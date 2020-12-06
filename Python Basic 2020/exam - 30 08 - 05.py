import sys
racer_name = input()
gold_cards = 0
silver_cards = 0
bronze_cards = 0
best_time = sys.maxsize
winner = ''
while racer_name != 'Finish':

    minutes = int(input())
    seconds = int(input())
    total_minutes = minutes * 60
    total_time = total_minutes + seconds
    if total_time < 55:
        gold_cards += 1
    elif 55 <= total_time <= 85:
        silver_cards += 1
    elif 85 < total_time <= 120:
        bronze_cards += 1
    if total_time <= best_time:
        best_time = total_time
        winner = racer_name
    racer_name = input()
total_minutes = best_time // 60
total_seconds = best_time % 60

print(f'With {total_minutes} minutes and {total_seconds} seconds {winner} is the winner of the day!')
print(f'Today\'s prizes are {gold_cards} Gold {silver_cards} Silver and {bronze_cards} Bronze cards!')