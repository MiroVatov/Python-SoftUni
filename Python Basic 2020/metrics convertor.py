digit_to_convert = float(input())
metric1 = input()
metric2 = input()
result = 0

mm_to_cm = 0.1
mm_to_meters = 0.001
cm_to_mm = 10
cm_to_m = 0.01
m_to_cm = 100
m_to_mm = 1000

if metric1 == 'm' and metric2 == 'cm':
    result = m_to_cm * digit_to_convert
elif metric1 == 'm' and metric2 == 'mm':
    result = m_to_mm * digit_to_convert
elif metric1 == 'cm' and metric2 == 'mm':
    result = cm_to_mm * digit_to_convert
elif metric1 == 'cm' and metric2 == 'm':
    result = cm_to_m * digit_to_convert
elif metric1 == 'mm' and metric2 == 'm':
    result = mm_to_meters * digit_to_convert
elif metric1 == 'mm' and metric2 == 'cm':
    result = mm_to_cm * digit_to_convert

print(f'{result:.3f}')



