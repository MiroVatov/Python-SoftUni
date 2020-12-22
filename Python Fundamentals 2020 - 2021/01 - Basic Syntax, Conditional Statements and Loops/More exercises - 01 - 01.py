num = input()

num = list(num)
num.sort(reverse=True)

string = ''

for i in num:
    string += i
print(string)