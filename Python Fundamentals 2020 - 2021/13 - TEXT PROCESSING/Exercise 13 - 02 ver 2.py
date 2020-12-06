text = input().split()

sum_chars = 0

str1 = text[0]
str2 = text[1]

shortest_word = min(text, key=len)
longest_word = max(text, key=len)

for ch in text:

    for a in shortest_word:
        if a == None:
            sum_chars += ord(a)
            pass
        else:
