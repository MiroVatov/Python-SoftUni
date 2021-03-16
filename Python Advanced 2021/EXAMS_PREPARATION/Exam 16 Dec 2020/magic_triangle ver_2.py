
def get_magic_triangle(n):
    triangle = []
    for i in range(1, n + 1):

        C = 1
        number_to_append = []
        for j in range(1, i + 1):
            number_to_append.append(C)
            C = C * (i - j) // j

        triangle.append(number_to_append)

    return triangle


print(get_magic_triangle(100))