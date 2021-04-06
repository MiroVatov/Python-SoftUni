
def fibonacci():
    n2 = 0
    n3 = 1
    while True:
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        yield n1


generator = fibonacci()
for i in range(5):
    print(next(generator))
