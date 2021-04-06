def fibonacci():
    a, b = 1, 0
    while True:
        a, b = b, a + b
        yield a


generator = fibonacci()
for i in range(5):
    print(next(generator))
