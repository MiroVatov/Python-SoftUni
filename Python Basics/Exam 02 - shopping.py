budget = float(input())
videocards = int(input())
processors = int(input())
ram_memory = int(input())

video_card_price = 250
processor_price = 0.35 * (videocards * video_card_price)
rams_price = 0.10 * (videocards * video_card_price)

total_expenses = (videocards * video_card_price) + (processors * processor_price) + (ram_memory * rams_price)

if videocards > processors:
    total_expenses = total_expenses * 0.85

if budget >= total_expenses:
    diff = budget - total_expenses
    print(f'You have {diff:.2f} leva left!')
else:
    diff = total_expenses - budget
    print(f'Not enough money! You need {diff:.2f} leva more!')