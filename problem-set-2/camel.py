def main():
    user = input("camelCase: ")
    (snake_case(user))


def snake_case(str):
    list1 = list(str)
    list2 = []

    for ch in list1:
        if ch.isupper():
            list2.append("_")
        list2.append(ch)

    snake_case = "".join(list2).lower()
    print("snake_case: {}".format(snake_case))



main()


"""
pseudocode:
convert the str into list of each character
declare a new list
loop through each character to check if it is capital
    if capital append underscore to the new list
append the capital character to the new list
join all the characters from the new list and assign it to the string
"""