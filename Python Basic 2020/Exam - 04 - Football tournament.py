football_team = input()
number_of_games = int(input())
total_points = 0
wins = 0
draws = 0
loses = 0
games = 0
for i in range(1, number_of_games + 1):
    result = input()
    games += 1
    if result == 'W':
        total_points += 3
        wins += 1
    elif result == 'D':
        total_points += 1
        draws += 1
    elif result == 'L':
        total_points += 0
        loses += 1

if games == 0:
    print(f'{football_team} hasn\'t played any games during this season.')
else:
    win_rate = (wins / games) * 100
    print(f'{football_team} has won {total_points} points during this season.')
    print(f'Total stats:')
    print(f'## W: {wins}')
    print(f'## D: {draws}')
    print(f'## L: {loses}')
    print(f'Win rate: {win_rate:.2f}%')