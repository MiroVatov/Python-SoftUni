special_symbols = ['.', ', ', "'", '-', '!', '?']

output_fh = open('output.txt', 'w')

with open('exercise02.txt', 'r') as file:

    for ind, line in enumerate(file):
        symbols = 0
        letters = 0
        for sym in special_symbols:
            symbols += line.count(sym)

        for let in line:
            if let.isalpha():
                letters += 1

        print(f"Line {ind + 1}: {line[:-2]} ({letters})({symbols})", file=output_fh)