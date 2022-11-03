import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if result := re.search(r"\"(http)(s?)(://)(www\.)?(youtu)(be).com/embed/([a-zA-Z0-9]+\")", s):
        url = (f"{result.group(1)}s{result.group(3)}{result.group(5)}.{result.group(6)}/{result.group(7)}")
        return url.strip('"')
    else:
        return None


if __name__ == "__main__":
    main()