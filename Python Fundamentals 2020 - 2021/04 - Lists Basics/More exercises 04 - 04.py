rows_num = int(input())

final_rows = []

for r in range(0, rows_num):

    final_rows.append([int(row) for row in input().split()])

attacked_squares = input().split()
destroyed_ships = 0

for i in attacked_squares:
    row_col = i.split("-")
    row = int(row_col[0])
    col = int(row_col[1])

    if final_rows[row][col] > 0:
        final_rows[row][col] -= 1
        if final_rows[row][col] == 0:
            destroyed_ships += 1
    else:
        continue


print(destroyed_ships)


