def main():
    user = input("")
    user = convert(user)
    print(user)

def convert(str):
    if (":)" and ":(" in str):
        str = str.replace(":)", "🙂")
        str = str.replace(":(", "🙁")
        return str
    elif ":)" in str:
        str = str.replace(":)", "🙂")
        return str
    elif ":(" in str:
        str = str.replace(":)", "🙁")
        return str

main()