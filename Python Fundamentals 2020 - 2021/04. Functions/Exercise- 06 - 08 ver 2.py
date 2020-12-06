
def loading_bar(number):

    lst_bar = []

    for n in range(10,  101, 10):
        if n % 10 == 0 and n <= number:
            lst_bar.append('%')
        else:
            lst_bar.append('.')

    if number < 100:
        print(f"{number}% [{''.join(lst_bar)}]")
        return f"Still loading..."
    else:
        print(f"{number}% Complete!")
        return f"[{''.join(lst_bar)}]"

num = int(input())

print(loading_bar(num))