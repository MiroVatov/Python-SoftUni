
special_symbols = ['.', ', ', ',', "'", '-', '!', '?']

output_fh = open('output.txt', 'w')

with open('text.txt', 'r') as file:

    for ind, line in enumerate(file, 1):
        symbols = [s for s in line if s in special_symbols]
        letters = [let for let in line if let.isalpha()]
        print(f"Line {ind}: {line[:-2]} ({len(letters)})({len(symbols)})", file=output_fh)

output_fh.close()
