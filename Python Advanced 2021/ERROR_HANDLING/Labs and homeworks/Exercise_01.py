numbers_dictionary = {}


line = input()

while line != "Search":
    #  Passing non-integer type to the variable number
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number

    except ValueError:
        print("The variable number must be an integer")

    line = input()

line = input()

while line != "Remove":
    #  Searching for a non - existent number
    searched = line
    try:
        print(numbers_dictionary[searched])

    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

line = input()

while line != "End":
    #  Removing a non-existent number

    searched = line
    try:
        del numbers_dictionary[searched]

    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)
