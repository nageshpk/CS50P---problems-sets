def main():
    user = input("What time is it? ")
    result = convert(user)
    if (result >= 7 and result <= 8):
        print("breakfast time")
    elif (result >= 12 and result <= 13):
        print("lunch time")
    elif (result >= 18 and result <= 19):
        print("dinner time")
    else:
        pass


def convert(time):
    x, y = time.split(":")
    # print(x, y)
    y = float(y) / 60
    z = float(x) + y
    return z



if __name__ == "__main__":
    main()