first_player_name = input()
second_player_name = input()
player1card = input()
player2card = ''
winner = ''
player1_total_points = 0
player2_total_points = 0
Number_wars = False
while player1card != 'End of game':

    player2card = input()
    player1card = int(player1card)
    player2card = int(player2card)
    player1points = 0
    player2points = 0
    if player1card == player2card:
        Number_wars = True
        print('Number wars!')
        player1card = int(input())
        player2card = int(input())
        if player1card > player2card:
            winner = first_player_name
            break
        elif player2card > player1card:
            winner = second_player_name
            break
    if player1card > player2card:
        player1points = player1card - player2card
    elif player2card > player1card:
        player2points = player2card - player1card

    player1_total_points += player1points
    player2_total_points += player2points
    player1card = input()

if Number_wars == True:
    if winner == first_player_name:
        print(f'{first_player_name} is winner with {player1_total_points} points')
    elif winner == second_player_name:
        print(f'{second_player_name} is winner with {player2_total_points} points')
else:

    print(f'{first_player_name} has {player1_total_points} points')
    print(f'{second_player_name} has {player2_total_points} points')