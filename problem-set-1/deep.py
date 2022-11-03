def main():
    user = input("What is the answer to the great question of life, the universe, and everything? ").strip().lower()
    user = check(user)


def check(str):
    if str == "42" or str == "forty-two" or str == "forty two":
        print("Yes")
    else:
        print("No")

main()