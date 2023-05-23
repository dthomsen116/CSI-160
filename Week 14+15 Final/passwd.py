import random
import time

big_list = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def make_user():
    global web
    web = input("What website is this Username used for? \n")
    global user
    user = input("Please enter your Username: \n")


def random_pass():
    with open("Words.txt", "r") as file:
        word_list = file.read()
        words = list(map(str, word_list.split()))

        random_word = random.choice(words)
        random_word2 = random.choice(words)
        global pass_word
        pass_word = (random_word.capitalize() + random_word2.capitalize() + str(random.randint(0, 999)))

        choice = input(pass_word + " is your randomised password. Would you like to keep this one or try for a new one? \n "
                          "If you would like to keep it, type: 'keep' \n "
                          "If you would like to make a new one, type: 'new' \n")
        if choice == "keep":
            pass_word
        elif choice == "new":
            random_pass()
        else:
            print("Wrong input, giving new password and trying again")
            random_pass()


def dict_enter():
    f = open("List.txt", "a")
    f.write(web + ", " + user + ", " + pass_word + ", " + "\n")
    f.close()


def read_dict():
    file = open("List.txt", "r")
    print(file.read())
    input("Press enter to continue")


def menu():
    ans = True
    while ans:
        print("""
        Please do steps 1-3 in order. 
        
        1.Make a User
        2.Make a Random Password
        3.Add Password to user
        4.Show the Account List
        5.Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            make_user()

        elif ans == "2":
            random_pass()

        elif ans == "3":
            dict_enter()

        elif ans == "4":
            read_dict()

        elif ans == "5":
            print("\n Goodbye")
            ans = None

        else:
            print("\n Not Valid Choice Try again")
            menu()

menu()
