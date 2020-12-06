tournament_name = input()

total_games = 0
total_games_won = 0
total_games_lost = 0
while tournament_name != 'End of tournaments':
    games_n = int(input())
    games_won = 0
    games_lost = 0
    game_number = 0
    for i in range(1, games_n + 1):
        Dessyteam_points = int(input())
        opponent_points = int(input())
        game_number += 1

        if Dessyteam_points > opponent_points:
            games_won += 1
            diff = Dessyteam_points - opponent_points
            print(f'Game {game_number} of tournament {tournament_name}: win with {diff} points.')
        else:
            games_lost += 1
            diff = opponent_points - Dessyteam_points
            print(f'Game {game_number} of tournament {tournament_name}: lost with {diff} points.')
    total_games_won += games_won
    total_games_lost += games_lost
    total_games += game_number
    tournament_name = input()

perc_won = (total_games_won / total_games) * 100
perc_lost = (total_games_lost / total_games) *  100

print(f'{perc_won:.2f}% matches win')
print(f'{perc_lost:.2f}% matches lost')