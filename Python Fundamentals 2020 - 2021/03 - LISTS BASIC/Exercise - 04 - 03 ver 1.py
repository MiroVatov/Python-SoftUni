red_cards = input()
lst = []
terminated = False
team_A_players = 11
team_B_players = 11
red_cards = red_cards.split()
last_player = ''
new_list = []
for i in red_cards:
    lst.append(i)

for i in lst:
    if 'A' in i and i not in new_list:
        team_A_players -= 1
    elif 'B' in i and i not in new_list:
        team_B_players -= 1
    new_list.append(i)

    if team_A_players < 7 or team_B_players < 7:
        terminated = True
        break
print(f'Team A - {team_A_players}; Team B - {team_B_players}')
if terminated:
    print(f'Game was terminated')

