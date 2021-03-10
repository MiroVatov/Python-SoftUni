def print_triangle(size):
    for row in range(1, size + 2):
        for i in range(1, row):
            print(i, end=' ')
        print()

    for row in range(size, 0, -1):
        for i in range(1, row):
            print(i, end=' ')
        print()





