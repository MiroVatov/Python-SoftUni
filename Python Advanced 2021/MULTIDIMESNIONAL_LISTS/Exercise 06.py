def is_valid(curr_pos, size):
    row = curr_pos[0]
    col = curr_pos[1]
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def kills_check(current_row, current_col, size, board):
    knights_killed = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        current_pos = [current_row + rows[i], current_col + cols[i]]
        if is_valid(current_pos, size) and board[current_pos[0]][current_pos[1]] == 'K':
            knights_killed += 1
    return knights_killed


n = int(input())

chess_board = [[e for e in input()] for _ in range(n)]
total_kills = 0
killed_knights = 0

while True:
    max_kills = 0
    to_kill = []

    for row in range(n):
        for col in range(n):
            position = chess_board[row][col]
            if position == 'K':
                killed_knights = kills_check(row, col, n, chess_board)

                if killed_knights > max_kills:
                    max_kills = killed_knights
                    to_kill = [row, col]

    if max_kills == 0:
        break

    to_kill_row = to_kill[0]
    to_kill_col = to_kill[1]
    chess_board[to_kill_row][to_kill_col] = '0'
    total_kills += 1

print(total_kills)