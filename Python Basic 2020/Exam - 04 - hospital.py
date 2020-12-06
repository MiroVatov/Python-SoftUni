period_days  = int(input())
doctors = 7
total_treated_patients = 0
total_untreated_patients = 0
for i in range(1, period_days + 1):
    treated_patients = 0
    untreated_patients = 0
    if i % 3 == 0:
        if total_untreated_patients > total_treated_patients:
            doctors += 1
    patients = int(input())
    if doctors >= patients:
        treated_patients += patients
    elif doctors < patients:
        untreated_patients = patients - doctors
        treated_patients = doctors
    total_treated_patients += treated_patients
    total_untreated_patients += untreated_patients
print(f'Treated patients: {total_treated_patients}.')
print(f'Untreated patients: {total_untreated_patients}.')