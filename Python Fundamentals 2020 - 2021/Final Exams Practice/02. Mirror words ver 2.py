import re
pattern = r"(@([A-Za-z]+){3}@@([A-Za-z]+){3}@)|(#([A-Za-z]+){3}##([A-Za-z]+){3}#)"
text = input()
match = re.findall(pattern, text)
list_with_words = []
for i in match:
    for j in i:
        if len(j) >= 10:
            list_with_words.append(j)
if len(list_with_words) < 1:
    print("No word pairs found!\nNo mirror words!")
elif len(list_with_words) > 0:
    print(f"{len(match)} word pairs found!")
    list_with_mirrors = []
    for i in list_with_words:
        split_symbol = ""
        if "#" in i:
            split_symbol += "#"
        else:
            split_symbol += "@"
        token = i.split(f"{split_symbol}")
        for i in token:
            if i == "":
                token.remove(i)
        word1 = token[0]
        word2 = token[1]
        list = []
        for j in range(len(word2)-1, -1, -1):
            list.append(word2[j])
        if word1 == "".join(list):
            list_with_mirrors.append(f"{word1} <=> {word2}")
    if len(list_with_mirrors) > 0:
        print("The mirror words are:")
        print(", ".join(list_with_mirrors))
    else:
        print("No mirror words!")