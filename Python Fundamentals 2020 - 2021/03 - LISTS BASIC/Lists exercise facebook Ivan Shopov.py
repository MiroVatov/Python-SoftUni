numbers = [1.23, 4.453, 2132.232, 2132.98]
formatted_numbers = ["%.2f" % number for number in numbers]
print(' '.join(str(number) for number in formatted_numbers))