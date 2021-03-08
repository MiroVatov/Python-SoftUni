# WITHOUT RECURSION --->

# def recursive_power(number, power):
#
#     return number ** power


def recursive_power(number, power):

    # Raise number to the power

    if power == 1:
        return number

    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
''''''
# start from the edge cases, where we don't have to call the function again.
''''''
# recursion steps ---->
# number ** power
# OR -> number ** 4
# OR -> number * (number ** 3)
# OR -> number * (number * (number ** 2))
# OR -> number * number * number * number



