key = int(input())
num_lines = int(input())

word = ''

for i in range(1, num_lines + 1):
    symbol = input()
    word += (ord(symbol) + key)

print(word)
