import emoji


def main():
    user = input("Input: ")
    val = emoji.emojize(user, language="alias")
    print(f"Output: {val}")

main()