all_cards = input().split(":")

instruct = input().split()

new_deck = [] * len(all_cards)

while instruct[0] != "Ready":

    command = instruct[0]

    if command == "Add":
        card_name = instruct[1]
        if card_name in all_cards:
            new_deck.append(card_name)
        else:
            print(f"Card not found.")

    elif command == "Insert":
        card_name = instruct[1]
        card_index = int(instruct[2])
        if card_name in all_cards:
            if 0 <= card_index < len(new_deck):
                new_deck.insert(card_index, card_name)
            else:
                print(f"Error!")

        else:
            print("Error!")

    elif command == "Remove":
        card_name = instruct[1]
        if card_name in new_deck:
            new_deck.remove(card_name)
        else:
            print("Card not found.")

    elif command == "Swap":

        card_1 = instruct[1]
        index_1 = new_deck.index(card_1)
        card_2 = instruct[2]
        index_2 = new_deck.index(card_2)
        if card_1 in new_deck and card_2 in new_deck:
            new_deck[index_1], new_deck[index_2] = new_deck[index_2], new_deck[index_1]

        # card_name = instruct[1]
        # card_name_2 = instruct[2]
        # for i, s in enumerate(new_deck):
        #     if card_name in s:
        #         new_deck[i] = s.replace(card_name, card_name_2)
        #     elif card_name_2 in s:
        #         new_deck[i] = s.replace(card_name_2, card_name)

  # elif command == "Shuffle":
    elif "Shuffle" in instruct and "deck" in instruct:
        new_deck.reverse()
      # new_deck = [card for card in reversed(new_deck)]
    instruct = input().split()

print(' '.join(new_deck))