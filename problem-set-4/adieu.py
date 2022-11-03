import inflect


def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            user = input("Name: ")
            names.append(user)
            list1 = p.join(names)
        except EOFError:
            print()
            print(f"Adieu, adieu, to", list1)
            break

main()