string = input()
rep = int(input())

def rep_str(string, rep):
    result = ''
    for i in range(rep):
        result += string

    return result

print(rep_str(string, rep))
