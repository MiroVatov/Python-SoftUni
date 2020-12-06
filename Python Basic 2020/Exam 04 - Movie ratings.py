import sys
max_rating = -sys.maxsize
min_rating = sys.maxsize
count_movies = 0
total_rating = 0
number_of_movies = int(input())
max_movie = ''
min_movie = ''
for i in range(1, number_of_movies + 1):
    movie_name = input()
    rating = float(input())
    count_movies += 1
    if rating > max_rating:
        max_rating = rating
        max_movie = movie_name
    if rating < min_rating:
        min_rating = rating
        min_movie = movie_name
    total_rating += rating
avg_rating = total_rating / count_movies

print(f'{max_movie} is with highest rating: {max_rating:.1f}')
print(f'{min_movie} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {avg_rating:.1f}')

