number_of_groups = int(input())
musala_people = 0
montblanc_people = 0
kilimanjaro_people = 0
k2_people = 0
everest_people = 0
total_people = 0
for i in range(1, number_of_groups + 1):
    people_per_group = int(input())

    if people_per_group <= 5:
        musala_people += people_per_group
    elif 6 <= people_per_group <= 12:
        montblanc_people += people_per_group
    elif 13 <= people_per_group <= 25:
        kilimanjaro_people += people_per_group
    elif 26 <= people_per_group <= 40:
        k2_people += people_per_group
    elif people_per_group >= 41:
        everest_people += people_per_group

    total_people += people_per_group
musala_perc = (musala_people / total_people) * 100
montblanc_perc = (montblanc_people / total_people) * 100
kilimanjaro_perc = (kilimanjaro_people / total_people) * 100
k2_perc = (k2_people / total_people) * 100
everest_perc = (everest_people / total_people) * 100


print(f'{musala_perc:.2f}%')
print(f'{montblanc_perc:.2f}%')
print(f'{kilimanjaro_perc:.2f}%')
print(f'{k2_perc:.2f}%')
print(f'{everest_perc:.2f}%')




