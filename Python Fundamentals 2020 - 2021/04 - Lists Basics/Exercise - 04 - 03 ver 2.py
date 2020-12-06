red_cards_str = input().split()

team_a = [1] * 11
team_b = [1] * 11
dismissed_players = []
sum_players_team_a = 11
sum_players_team_b = 11

for card in red_cards_str:
    tokens = card.split('-')
    team = tokens[0]
    player = int(tokens[1])

    if team == 'A' and tokens not in dismissed_players:
        team_a[player - 1] = 0
        sum_players_team_a -= 1
        if sum_players_team_a < 7:
            break
    elif team == 'B' and tokens not in dismissed_players:
        team_b[player - 1] = 0
        sum_players_team_b -= 1
        if sum_players_team_b < 7:
            break
    dismissed_players.append(tokens)


team_a_count = 0
team_b_count = 0

for i in range(11):
    team_a_count += team_a[i]
    team_b_count += team_b[i]


#team_a_count = team_a.count(1)
#team_b_count = team_b.count(1)
print(f'Team A - {team_a_count}; Team B - {team_b_count}')

if sum_players_team_a < 7 or sum_players_team_b < 7:
    print(f'Game was terminated')