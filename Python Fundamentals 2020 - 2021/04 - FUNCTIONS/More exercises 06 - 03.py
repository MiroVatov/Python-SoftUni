import math

def biggest():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())


    diff_x1_y1 = abs(x1) + abs(y1)
    diff_x2_y2 = abs(x2) + abs(y2)
    diff_x1_y1_x2_y2 = abs(x1) + abs(y1) + abs(x2) + abs(y2)


    x3 = float(input())
    y3 = float(input())
    x4 = float(input())
    y4 = float(input())

    diff_x3_y3 = abs(x3) + abs(y3)
    diff_x4_y4 = abs(x4) + abs(y4)
    diff_x3_y3_x4_y4 = abs(x3) + abs(y3) + abs(x4) + abs(y4)


    if diff_x1_y1_x2_y2 > diff_x3_y3_x4_y4:

        if diff_x1_y1 <= diff_x2_y2:
            print(f'({math.floor(int(x1))}, {math.floor(int(y1))})({math.floor(int(y2))}, {math.floor(int(y2))}')
        else:
            print(f'({math.floor(int(x2))}, {math.floor(int(y2))})({math.floor(int(x1))}, {math.floor(int(y1))}')

    elif diff_x3_y3_x4_y4 > diff_x1_y1_x2_y2:

        if diff_x3_y3 <= diff_x4_y4:
            print(f'({math.floor(int(x3))}, {math.floor(int(y3))})({math.floor(int(x4))}, {math.floor(int(y4))})')
        else:
            print(f'({math.floor(int(x4))}, {math.floor(int(y4))})({math.floor(int(x3))}, {math.floor(int(y3))})')
    else:
        if diff_x1_y1 <= diff_x2_y2:
            print(f'({math.floor(int(x1))}, {math.floor(int(y1))})({math.floor(int(y2))}, {math.floor(int(y2))})')
        else:
            print(f'({math.floor(int(x2))}, {math.floor(int(y2))})({math.floor(int(x1))}, {math.floor(int(y1))})')

biggest()