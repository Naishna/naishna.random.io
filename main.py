import random


def guess(x):
    ranNum = random.randint(1, x)
    guess = 0
    while guess != ranNum:
        guess = int(input("Enter your number "))
        if guess > ranNum:
            print("Too high number")
        elif guess < ranNum:
            print("Too low number")

    print("That's the right number!")


x = int(input("Enter the limit of number "))
guess(x)
