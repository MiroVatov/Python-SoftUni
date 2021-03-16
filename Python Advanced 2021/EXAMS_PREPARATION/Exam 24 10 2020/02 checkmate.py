def valid_move(row, col, limit):
    if 0 <= row < limit and 0 <= col < limit:
        return True
    return False


chess_board = [[el for el in input().split()] for el in range(8)]

queen_moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

KING = 'K'
QUEEN = 'Q'
EMPTY_POS = '.'
BOARD_LIMIT = 8

queens_positions = []

# Make refactoring to search for the KING and then to make the search for the Queens !!!!!!!!!!!!!!!!!!

for row in range(len(chess_board)):
    for col in range(len(chess_board[row])):
        king_found = False

        if chess_board[row][col] == QUEEN:

            for move in queen_moves:
                current_row, current_col = row, col
                current_row += move[0]
                current_col += move[1]

                while valid_move(current_row, current_col, BOARD_LIMIT):

                    if chess_board[current_row][current_col] == KING:
                        queens_positions.append([row, col])
                        king_found = True
                        break
                    elif chess_board[current_row][current_col] == QUEEN:
                        break

                    current_row += move[0]
                    current_col += move[1]

                if king_found:
                    break


            # if QUEEN on our way -> break
            # if some of the row index or col index out of the chess_board -> break
            # if KING on our way -> keep the Queen indexes -> break

if not queens_positions:
    print(f"The king is safe!")
else:
    for line in queens_positions:
        print(line)

# Make refactoring to search for the KING and then to make the search for the Queens
