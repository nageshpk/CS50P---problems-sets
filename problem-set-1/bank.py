def main():
    user = input("Greeting: ").strip().lower()
    check(user)


def check(str):
    if str[0:5] == "hello":
        print("$0")
    elif str[0] == "h" and str != "hello":
        print("$20")
    else:
        print("$100")

main()