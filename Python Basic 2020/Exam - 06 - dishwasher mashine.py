bottles_qty = int(input())
deterget_in_militer = bottles_qty * 750

dishes = input()
cycle = 0
pots_qty = 0
plates_qty = 0

while dishes != 'End':
    dishes = int(dishes)
    cycle += 1
    if cycle % 3 == 0:
        pots_qty += dishes
        deterget_in_militer = deterget_in_militer - (dishes * 15)
    else:
        plates_qty += dishes
        deterget_in_militer = deterget_in_militer - (dishes * 5)
    if deterget_in_militer < 0:
        print(f'Not enough detergent, {abs(deterget_in_militer)} ml. more necessary!')
        break
    dishes = input()
if deterget_in_militer >= 0:
    print(f'Detergent was enough!')
    print(f'{plates_qty} dishes and {pots_qty} pots were washed.')
    print(f'Leftover detergent {deterget_in_militer} ml.')

