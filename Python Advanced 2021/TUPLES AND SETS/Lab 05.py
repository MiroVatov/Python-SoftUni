number_of_invited_guests = int(input())

invited_guests_lst = []

for _ in range(number_of_invited_guests):
    invited_guests_lst.append(input())

guests_attend = []

while True:
    guest = input()
    if guest == 'END':
        break
    guests_attend.append(guest)

guests_not_came = []

for guest in invited_guests_lst:
    if guest not in guests_attend:
        guests_not_came.append(guest)

print(len(guests_not_came))
for g in sorted(guests_not_came):
    print(g)



