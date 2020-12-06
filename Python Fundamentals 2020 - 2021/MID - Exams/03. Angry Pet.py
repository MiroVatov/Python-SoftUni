def validity_checker(sum_rating, type_rating, type_item, entry_point_r):
    if (type_rating == "positive" or type_rating == "all") and type_item == "cheap" and (sum_rating < entry_point_r and sum_rating >= 0):
        return True
    elif (type_rating == "negative") and type_item == "cheap" and (sum_rating < entry_point_r and sum_rating < 0):
        return True
    elif (type_rating == "positive" or type_rating == "all") and type_item == "expensive" and (sum_rating >= entry_point_r and sum_rating >= 0):
        return True
    elif (type_rating == "negative") and type_item == "expensive" and (sum_rating < entry_point_r and sum_rating >= 0):
        return True


price_ratings = [int(i) for i in input().split()]
entry_point = int(input())

type_of_items = input()
type_of_ratings = input()
left_sum = 0
right_sum = 0

left_cycle = price_ratings[:entry_point]
right_cycle = price_ratings[entry_point + 1:]

entry_point_break = price_ratings[entry_point]

for a in range(len(left_cycle)):
    rating = left_cycle[a]
    if validity_checker(rating, type_of_ratings, type_of_items, entry_point_break):
        left_sum += left_cycle[a]

for b in range(len(right_cycle)):
    rating = right_cycle[b]
    if validity_checker(rating,  type_of_ratings, type_of_items, entry_point_break):
        right_sum += price_ratings[b]

if left_sum >= right_sum:
    print(f"Left - {left_sum}")
else:
    print(f"Right - {right_sum}")