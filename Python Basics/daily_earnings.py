working_days = int(input())
money_per_day = float(input())
usd_to_lev_rate = float(input())

month_salary = working_days * money_per_day
yearly_income_plus_bonuses = (month_salary * 12) + (month_salary * 2.5)
yearly_tax = 0.25 * yearly_income_plus_bonuses
total_year_income = yearly_income_plus_bonuses - yearly_tax
total_year_income_to_leva = total_year_income * usd_to_lev_rate
profit_per_day = total_year_income_to_leva / 365

print(f'{profit_per_day:.2f}')