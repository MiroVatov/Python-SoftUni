skumria_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
mussles_kg = float(input())

mussels_price = 7.50
palamud_price = skumria_price + skumria_price * 0.60
safrid_price = caca_price + caca_price * 0.80

palamud_total = palamud_kg * palamud_price
safrid_total = safrid_kg * safrid_price
mussels_total = mussles_kg * mussels_price
total = palamud_total + safrid_total + mussels_total
print(f'{total:.2f}')