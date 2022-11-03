import sys
import random

def main():
    level = get_level()
    questions = 10
    score = 0
    while questions > 0:
        questions -= 1
        x, y = get_int(level)
        summation = x + y
        attempt = 0
        while attempt < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer != summation:
                    print("EEE")
                    attempt += 1
                    continue
                else:
                    score += 1
                    break
            except ValueError:
                print("EEE")
                attempt += 1
                continue
        else:
            print(f"{x} + {y} = {summation}")
    print(f"Score: {score}")



def get_int(num):
    if num == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif num == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif num == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level < 4:
                break
        except ValueError:
            continue
    return level


if __name__ == "__main__":
    main()