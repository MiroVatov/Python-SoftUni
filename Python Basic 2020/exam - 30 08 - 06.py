strawberries = 0
raspberries = 0
rows_num = int(input())
positions = int(input())
total_amount = 0

for rows in range(1, rows_num + 1):
    if rows % 2 != 0:
        for pos in range(1, positions + 1):
                strawberries += 3.50
    if rows % 2 == 0:
        for pos in range(1, positions + 1):
            if pos % 3 != 0:
                raspberries += 5

total_amount = (strawberries + raspberries) * 0.80

print(f'Total: {total_amount:.2f} lv.')