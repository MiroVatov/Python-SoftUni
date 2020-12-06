import math

def closest():

    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    diff_x1_y1 = abs(x1) + abs(y1)
    diff_x2_y2 = abs(x2) + abs(y2)

    if diff_x1_y1 < diff_x2_y2:
        print(f'({math.floor(int(x1))}, {math.floor(int(y1))})')

    elif diff_x2_y2 < diff_x1_y1:
        print(f'({math.floor(int(x2))}, {math.floor(int(y2))})')

    else:
        print(f'({math.floor(int(x1))}, {math.floor(int(y1))})')

closest()



