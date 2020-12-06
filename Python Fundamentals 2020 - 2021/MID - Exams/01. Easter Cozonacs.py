budget = float(input())

price_per_kilo_flour = float(input())
pack_of_eggs = price_per_kilo_flour * 0.75
quarter_milk = (price_per_kilo_flour * 1.25) / 4
cozunac_price = pack_of_eggs + price_per_kilo_flour + quarter_milk
colored_eggs = 0
cozunacs_count = 0

while budget >= cozunac_price:
    cozunacs_count += 1
    colored_eggs += 3
    budget -= cozunac_price
    if cozunacs_count % 3 == 0:
        eggs_loss = cozunacs_count - 2
        colored_eggs -= eggs_loss

print(f"You made {cozunacs_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")