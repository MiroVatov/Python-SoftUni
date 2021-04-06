def genrange(start, end):
    range_iterable = list(range(start, end + 1))

    while start <= end:
        yield start
        start += 1


print(list(genrange(1, 10)))

# Variant 2 -- >> built in generator expression : (x for x in range(20))

gen = (x for x in range(20))
print(list(gen))


# TODO finish the code below

def gen(num):
    return (x for x in range(num))

