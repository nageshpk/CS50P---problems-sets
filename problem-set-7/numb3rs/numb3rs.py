import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if ip.isalpha():
        return False
    else:
        if matches := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
            value = 0
            for group in matches.groups():
                if int(group) <= 255:
                    value += 1

            if value == 4:
                return True
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    main()