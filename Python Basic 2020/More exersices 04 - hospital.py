period_days = int(input())
doctor_number = 7
total_threated_patients = 0
total_unthreated_patienst = 0

for i in range(1, period_days + 1):
    daily_threated_patients = 0
    daily_unthreated_patients = 0

    if i % 3 == 0 and total_unthreated_patienst > total_threated_patients:
        doctor_number += 1
    patients_count = int(input())

    if doctor_number >= patients_count:
        daily_threated_patients = patients_count
        daily_unthreated_patients = 0
    if doctor_number < patients_count:
        daily_unthreated_patients = patients_count - doctor_number
        daily_threated_patients = patients_count - daily_unthreated_patients

    total_threated_patients += daily_threated_patients
    total_unthreated_patienst += daily_unthreated_patients

print(f'Treated patients: {total_threated_patients}.')
print(f'Untreated patients: {total_unthreated_patienst}.')







