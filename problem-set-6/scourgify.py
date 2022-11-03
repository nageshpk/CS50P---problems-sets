import csv
import sys


def main():
    if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a csv file")
    else:
        try:
            list1 = read_file()
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
        else:
            write_to(list1)


def read_file():
    dicts = []
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row['name'].split(",")
            dicts.append({'first': first.lstrip(), 'last': last.lstrip(), 'house': row['house']})
    return dicts


def write_to(list):
    with open(sys.argv[2], 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for dict in list:
            writer.writerow({'first': dict['first'], 'last': dict['last'], 'house': dict['house']})


main()