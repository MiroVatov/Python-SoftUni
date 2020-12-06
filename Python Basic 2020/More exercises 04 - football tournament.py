stadium_capacity = int(input())
fans = int(input())

total_sector_A = 0
total_sector_B = 0
total_sector_V = 0
total_sector_G = 0
for i in range(1, fans + 1):
    sector = input()
    if sector == 'A':
        total_sector_A += 1
    elif sector == 'B':
        total_sector_B += 1
    elif sector =='V':
        total_sector_V += 1
    elif sector == 'G':
        total_sector_G += 1

total_fans = total_sector_A + total_sector_B + total_sector_V + total_sector_G

total_fans_perc = (total_fans / stadium_capacity) * 100
sector_A_perc = (total_sector_A / total_fans) * 100
sector_B_perc = (total_sector_B / total_fans) * 100
sector_V_perc = (total_sector_V / total_fans) * 100
sector_G_perc = (total_sector_G / total_fans) * 100

print(f'{sector_A_perc:.2f}%')
print(f'{sector_B_perc:.2f}%')
print(f'{sector_V_perc:.2f}%')
print(f'{sector_G_perc:.2f}%')
print(f'{total_fans_perc:.2f}%')