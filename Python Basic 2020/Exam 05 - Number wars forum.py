player_one = input()
player_two = input()

result_player_one = 0
result_player_two = 0

input_text = input()

while input_text != "End of game":
    card_player_one = int(input_text)
    card_player_two = int(input())

    if card_player_one > card_player_two:
        result_player_one += (card_player_one - card_player_two)

    if card_player_two > card_player_one:
        result_player_two += (card_player_two - card_player_one)

    if card_player_one == card_player_two:
        print("Number wars!")
        card_player_one = int(input())
        card_player_two = int(input())

        if card_player_one > card_player_two:
            print(f"{player_one} is winner with {result_player_one} points")
            break
        if card_player_one < card_player_two:
            print(f"{player_two} is winner with {result_player_two} points")
            break

    input_text = input()

if input_text == "End of game":
    print(f"{player_one} has {result_player_one} points")
    print(f"{player_two} has {result_player_two} points")