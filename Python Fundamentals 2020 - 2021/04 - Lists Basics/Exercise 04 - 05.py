text = input().split()

shuffles = int(input())
middle = int(len(text) / 2)
final_text = []
counter = 0

for i in range(shuffles):
    final_text = []
    for a in range(0, middle):
        final_text.append(text[a])

        for b in range(middle, len(text)):
            final_text.append(text[b])
            if b >= middle:
                break
        middle += 1
    middle = int(len(text) / 2)
    text = final_text

print(text)