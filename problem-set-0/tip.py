def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    # print(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # print(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    str, Float = d.split("$")
    Float = float(Float)
    return Float


def percent_to_float(p):
    cent, str = p.split("%")
    cent = float(cent) / 100
    return cent



main()