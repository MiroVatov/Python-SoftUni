gifts = input().split()

command = input()

while command != 'No Money':

    gifts_lst = command.split()
    command = gifts_lst[0]
    gift = gifts_lst[1]

    if command == 'OutOfStock':
        if gift in gifts:
            for i in range(len(gifts)):
                if gift in gifts[i]:
                    gifts[i] = 'None'

    elif command == 'Required':

        command = gifts_lst[0]
        gift = gifts_lst[1]
        index = int(gifts_lst[2])
        if index < len(gifts) and index >= 0:

            gifts[index] = gift

    elif command == 'JustInCase':
        gifts[-1] = gift

    command = input()

final_str = []
string = ''

for ind in gifts:
    if ind is not 'None':
        final_str.append(ind)
        string += (ind + ' ')

print(string, end='')

