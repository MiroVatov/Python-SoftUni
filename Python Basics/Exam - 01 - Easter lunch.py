easter_bread_price = 3.20
twelve_eggs_price = 4.35
cookies_price = 5.40
egg_paint_per_egg = 0.15

num_easter_breads = int(input())
num_eggshells = int(input())
num_cookies = int(input())

total_bill = (easter_bread_price * num_easter_breads) + ((twelve_eggs_price * num_eggshells) + ((num_eggshells ) * 12) * egg_paint_per_egg) + (cookies_price * num_cookies)

print(f'{total_bill:.2f}')