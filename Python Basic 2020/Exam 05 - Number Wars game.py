first_player_name = input()
second_player_name = input()

player1_total_points = 0
player2_total_points = 0
input_text = input()
while input_text != 'End of game':
    player1card = int(input_text)
    player2card = int(input())
    player1points = 0
    player2points = 0
    if player1card > player2card:
        player1points = player1card - player2card
    player1_total_points += player1points
    if player2card > player1card:
        player2points = player2card - player1card
    player2_total_points += player2points
    if player1card == player2card:
        print('Number wars!')
        player1card = int(input())
        player2card = int(input())
        if player1card > player2card:
            print(f'{first_player_name} is winner with {player1_total_points} points')
            break
        elif player2card > player1card:
            print(f'{second_player_name} is winner with {player2_total_points} points')
            break

    input_text = input()

if input_text == 'End of game':
    print(f'{first_player_name} has {player1_total_points} points')
    print(f'{second_player_name} has {player2_total_points} points')