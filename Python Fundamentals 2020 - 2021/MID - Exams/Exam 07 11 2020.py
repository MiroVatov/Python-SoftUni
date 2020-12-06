import math
budget = float(input())
students_num = int(input())
flour_price_package = float(input())
egg_price = float(input())
arpon_price = float(input())

arpons = (math.ceil(students_num * 0.20) + students_num) * arpon_price
eggs = (egg_price * 10) * students_num
free_flour = students_num // 5
flour = flour_price_package * (students_num - free_flour)


needed_budget = arpons + eggs + flour

if needed_budget <= budget:
    print(f"Items purchased for {needed_budget:.2f}$.")
else:
    diff = needed_budget - budget
    print(f"{diff:.2f}$ more needed.")