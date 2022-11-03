def main():
    user = input("Expression: ")
    out = result(user)
    print(f"{out:.1f}")

def result(str):
    x, y, z = str.split(" ")
    if y == "+":
        return float(x) + float(z)
    elif y == "-":
        return float(x) - float(z)
    elif y == "*":
        return float(x) * float(z)
    elif y == "/":
        return float(x) / float(z)
    else:
        pass


main()