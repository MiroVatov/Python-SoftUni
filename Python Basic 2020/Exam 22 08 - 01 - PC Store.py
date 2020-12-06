processor_price = float(input())
videocard_price = float(input())
ram_price = float(input())
rams_qty = int(input())
discount_perc = float(input())
discount_perc = discount_perc * 100
processor_price = (processor_price * 1.57)
videocard_price = (videocard_price * 1.57)
ram_price = ((ram_price * rams_qty) * 1.57)
processor_price = processor_price - ((discount_perc * processor_price) / 100)
videocard_price = videocard_price - ((discount_perc * videocard_price) / 100)
total_price_disc = (processor_price + videocard_price + ram_price)


print(f'Money needed - {total_price_disc:.2f} leva.')