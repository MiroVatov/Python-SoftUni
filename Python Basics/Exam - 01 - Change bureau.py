num_bitcoins = int(input())
num_chinese_yuans = float(input())
commission_pct = float(input())

one_bitcoin_to_lev = 1168
one_chinese_yuan_to_usd = 0.15
one_usd_to_lev = 1.76
one_eur_to_lev = 1.95

total_bitcoins_leva = num_bitcoins * one_bitcoin_to_lev
total_yuans_to_leva = num_chinese_yuans * one_chinese_yuan_to_usd

total_money_to_leva = (total_yuans_to_leva * 1.76) + (total_bitcoins_leva)
total_money_to_eur = (total_money_to_leva / 1.95)
total_commission = (total_money_to_eur * (commission_pct / 100))
final_conversion = total_money_to_eur - total_commission

print(f'{final_conversion:.2f}')