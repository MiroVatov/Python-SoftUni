from math import floor

income = float(input())
average_note = float(input())
min_income = float(input())

social_scholarship = 0
nerd_scholarship = 0

if income < min_income and average_note > 4.5:
    social_scholarship = min_income * 0.35

if average_note >= 5.5:
    nerd_scholarship = average_note * 25

if nerd_scholarship > social_scholarship:
    print(f'You get a scholarship for excellent results {floor(nerd_scholarship)} BGN')
elif social_scholarship > nerd_scholarship:
    print(f'You get a Social scholarship {floor(social_scholarship)} BGN')
else:
    print(f'You cannot get a scholarship!')