import math

year_type = input()
vacation_days_count = int(input()) # брой празници в годината (които не са събота и неделя);
weekends_in_hometown = int(input()) # брой уикенди, в които Влади си пътува до родния град

total_games_played = 0
# 48 free weekends

weekends_in_Sofia = 48 - weekends_in_hometown


total_games_played = 3/4 * (weekends_in_Sofia)
total_games_played += 2/3 * vacation_days_count
total_games_played += weekends_in_hometown

if year_type == 'normal':
    print(math.floor(total_games_played))
elif year_type == 'leap':
    total_games_played += 0.15 * total_games_played
    print(math.floor(total_games_played))