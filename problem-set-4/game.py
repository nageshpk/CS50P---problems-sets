import random
import sys


def get_random(s):
    integer = random.randint(1, s)
    return integer


while True:
    n = input("Level: ")
    if n.isdigit() and int(n) > 0:
        x = get_random(int(n))
        while True:
            try:
                guess = int(input("Guess: "))
                if guess < x:
                    print("Too small!")
                    continue
                elif guess > x:
                    print("Too large!")
                    continue
                else:
                    sys.exit("Just right!")
            except ValueError:
                continue
    else:
        continue