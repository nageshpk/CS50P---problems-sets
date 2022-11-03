def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def check_zero(s):
    str = ""
    for i in s:
        if i.isdigit():
            str += i
            if str[0] == "0":
                return False
            else:
                return True


def check_number(s):
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i:].isdigit():
                return True
            else:
                return False


def is_valid(s):
    if len(s) > 1 and len(s) <= 6 and s[:2].isalpha():
        if s.isalpha():
            return True
        elif s.isalnum():
            if s[-1].isdigit() and check_zero(s) and check_number(s):
                for ch in s:
                    if ch.isalpha():
                        return True
                    elif ch.isdigit() and ch != "0":
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False


main()
