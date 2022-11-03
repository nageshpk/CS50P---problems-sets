def main():
    user = input("Input: ")
    check(user)


def check(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str1 = ""
    for i in str:
        if i.lower() not in vowels:
            str1 += i
        else:
            str
    print(f"Output: {str1}")


main()