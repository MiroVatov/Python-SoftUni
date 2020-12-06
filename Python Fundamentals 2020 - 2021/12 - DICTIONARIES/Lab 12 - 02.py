elements = input().split(" ")

pairs_dict = {}

for ind in range(0, len(elements), 2):
        pairs_key = elements[ind]
        value = elements[ind + 1]
        pairs_dict[pairs_key] = value

search = input().split(" ")

for i in search:
        if i in pairs_dict:
                quantity = pairs_dict[i]
                print(f"We have {quantity} of {i} left")

        else:
                print(f"Sorry, we don't have {i}")