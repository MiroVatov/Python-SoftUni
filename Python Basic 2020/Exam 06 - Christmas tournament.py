tournament_days = int(input())
days_winner = 0
days_loser = 0

total_money_earned = 0

for i in range(1, tournament_days + 1):
    command = input()
    money_won = 0
    games_won = 0
    games_lost = 0
    while command != 'Finish':
        outcome = input()
        if outcome == 'win':
            games_won += 1
            money_won += 20
        elif outcome == 'lose':
            games_lost += 1
        command = input()
    if games_won > games_lost:
        money_won = money_won + (money_won * 0.10)
        days_winner += 1
    else:
        days_loser += 1
    total_money_earned += money_won

if days_winner > days_loser:
    total_money_earned = total_money_earned + total_money_earned * 0.20
    print(f'You won the tournament! Total raised money: {total_money_earned:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money_earned:.2f}')


