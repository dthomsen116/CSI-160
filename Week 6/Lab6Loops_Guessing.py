import random

randomNum = random.randint(0, 100)

def rng_guess():

    user = int(input("Please guess a number between 0 and 100: "))

    if user == randomNum:
        print("You guessed correctly!")
        exit()

    elif user > 100:
        print("Out of bounds. Guess between 0 and 100")
        rng_guess()

    elif user <= -1:
        print("Out of bounds. Why are you guessing negative numbers? This is why humans cry.")
        rng_guess()

    elif user > randomNum:
        print("Wrong answer, Value is too high. Try again.")
        rng_guess()

    elif user < randomNum:
        print("Wrong answer, Value is too low. Try again.")
        rng_guess()



rng_guess()
