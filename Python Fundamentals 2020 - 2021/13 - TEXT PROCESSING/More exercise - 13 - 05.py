title_of_an_article = input()
print(f"<h1>")
print(title_of_an_article)
print(f"</h1>")
content_of_the_article = input()
print(f"<article>")
print(content_of_the_article)
print(f"</article>")

while True:

    comment = input()

    if comment == "end of comments":
        break
    print(f"<div>")
    print(comment)
    print(f"</div>")