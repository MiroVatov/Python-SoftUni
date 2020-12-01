movie_name = input()
days = int(input())
tickets_number = int(input())
ticket_price = float(input())
percent_for_cinema = int(input())

total_profit = (days * tickets_number * ticket_price)
percent_for_cinema = (total_profit * percent_for_cinema) / 100

print(f'The profit from the movie {movie_name} is {total_profit - percent_for_cinema:.2f} lv.')


print(f'{percent_for_cinema:.2f}')