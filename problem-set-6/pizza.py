from tabulate import tabulate
import csv
import sys


def main():
    get_pizza()


def get_pizza():
    if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a csv file")
    else:
        try:
            with open(sys.argv[1], 'r') as file:
                reader = csv.reader(file)
                list1 = get_list(reader)
                print(tabulate(list1, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")


def get_list(content):
    list1 = []
    for row in content:
        list1.append(row)
    return list1


main()