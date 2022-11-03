def main():
    get_dict("")


def compute(item, dict):
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
    return dict


### sort the dictinary
def sort_dict(dict):
    for i in sorted(dict):
        print(dict[i], i.upper())


def get_dict(prompt):
    dict = {}
    while True:
        try:
            item = input(prompt)
            dict = compute(item, dict)
        except (EOFError, KeyError):
            break
    sort_dict(dict)


main()