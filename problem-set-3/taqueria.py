menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0
    get_total("Item: ", total)


def get_total(propmt, total):
    while True:
        try:
            item = input(propmt).title()
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
        except (EOFError, KeyError):
            print("")
            break


main()