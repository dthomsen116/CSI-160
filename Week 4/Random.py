import random


def rng_guess():

    randomNum = random.randint(0, 9)

    user = int(input("Please guess a number between 0 and 9: "))

    if user == randomNum:
        print("You guessed correctly!")
    else:
        print("Wrong answer. Try again.")
        rng_guess()
