import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a python file")
    else:
        try:
            with open(sys.argv[1], 'r') as file:
                content = file.readlines()
                lines = get_row_list(content)
                print(len(lines))
        except FileNotFoundError:
            sys.exit("File does not exist")


def get_row_list(rows):
    lines = []
    for row in rows:
        if not row.lstrip().startswith("#") and not row.isspace():
            lines.append(row)
    return lines


main()