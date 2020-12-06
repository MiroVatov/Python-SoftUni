import collections
tickets = input().split(", ")

for ticket in tickets:
    left_winner = False
    right_winner = False
    winner = []
    left_half = ''
    right_half = ''
    ticket = [i for i in ticket if i != ' ']

    if len(ticket) == 20:
        middle = len(ticket) // 2
        left_half = ticket[0:middle:]
        right_half = ticket[middle::]
        counter = 0
        winning_symbol = [s for s in left_half if s == "@" or s == "#" or s == "$" or s == "^"]
        winning_symbol = [item for item, count in collections.Counter(winning_symbol).items() if count >= 6]
        winning_symbol = ''.join(winning_symbol)
        winner_left = []
        for l in left_half:
            if l == winning_symbol:
                winner_left.append(l)
                counter += 1
                if 6 <= len(winner_left) <= 10 and counter >= 6:
                    left_winner = True
            else:
                counter = 0

        counter = 0
        winner_right = []
        for r in right_half:
            if r == winning_symbol:
                winner_right += r
                counter += 1
                if 6 <= len(winner_right) <= 10 and counter >= 6:
                    right_winner = True
            else:
                counter = 0

        if left_winner and right_winner and (6 <= len(winner_left) <= 10 and 6 <= len(winner_right) <= 10):

            if 6 <= len(winner_left) <= 9 and 6 <= len(winner_right) <= 9:
                final_winner = min(winner_right, winner_left)
                print(f"ticket \"%s\"" % f"{''.join(ticket)}", end='')
                print(f" - {len(final_winner)}{winning_symbol}")

            elif (6 <= len(winner_left) <= 9 and 6 <= len(winner_right) == 10) or (6 <= len(winner_right) <= 9 and 6 <= len(winner_left) == 10):
                final_winner = min(winner_right, winner_left)
                print(f"ticket \"%s\"" % f"{''.join(ticket)}", end='')
                print(f" - {len(final_winner)}{winning_symbol}")

            elif len(winner_left) == 10 and len(winner_right) == 10:
                print(f"ticket \"%s\"" % f"{''.join(ticket)}", end='')
                print(f" - {len(winner_left)}{winning_symbol} Jackpot!")

        else:
            print(f"ticket \"%s\"" % f"{''.join(ticket)}", end='')
            print(" - no match")
    else:
        print(f"invalid ticket")
