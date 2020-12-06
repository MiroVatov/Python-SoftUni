one_leva_coins_number = int(input())
two_leva_coins_number = int(input())
five_leva_banknotes_number = int(input())
total_sum = int(input())
sum_money = 0
count_one_leva = 0
count_two_leva = 0
count_five_leva = 0

for one in range(1, one_leva_coins_number + 1):

    for two in range(1, two_leva_coins_number + 1):

        for five in range(1, five_leva_banknotes_number + 1):

            
            if sum_money == total_sum:
                print(f'{count_one_leva} * 1 lv. + {count_two_leva} * 2 lv. + {count_five_leva} * 5 lv. = {total_sum} lv.')
