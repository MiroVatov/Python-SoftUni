key = int(input())
n = int(input())

word = ''

for i in range(n):
    char = input()
    letter = (ord(char) + key)
    word += chr(letter)

print(word)
