"""Write  a program that has a conversation with the user.
The program must ask for strings, integers and floats as input.
The program must ask for at least 4 different inputs from the user.
The program must reuse at least 4 of these inputs in what it displays on the screen.
The program must perform at least 2 arithmetic operations on the numbers the user inputs.


Author: David Thomsen
Class: CSI-160
Assignment:Conversation With a Computer
Due Date: 9/13/21

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

name = input("What is your name? : ")
input("Thank you, " + name + ". I'm David. How are You? : ")
age = input("How old are you? : ")


""" This input asks the user how old they are then depending on the response it will give agreeing responses."""


if int(age) >= (18):
    input("Conrgats! You're old enough to vote! Did you? (Please respond with 'yes' or 'no') : ")

elif int(age) < (18):
    input("You're to young to vote! Do you want to vote in the next election? (Please respond with 'yes' or 'no') : ")

else:
    print("Please enter a whole number and try again")

siblings = input("How many siblings do you have, " + name + "? : ")
brothers = input("How many are brothers? : ")

num_sib = int(siblings)
num_bro = int(brothers)


"""This just turns the original variables into int values in order to be subtracted from each other. """


bone = input("Oh, so you have " + str(num_bro) + " brother(s), and " + str((num_sib - num_bro)) +
             " sister(s). Cool. Have you ever broken a bone before? (Please respond with 'yes' or 'no') : ")
if bone == "yes":

    broken = input("How many bones have you broken? : ")
    bones_broke = int(broken)
    if bones_broke == 1:
        input("That's the same as me! What number is your house on your street?")
    else:
        input("That's " + str((bones_broke - 1)) + " more than me! What number is your house on your street? : ")

elif bone == "no":
    input("I can tell you drink your milk! What number is your house on your street? : ")
else:
    print("Please respond with 'yes' or 'no' and try again")

state = input("What state are you from? (please format as two letter abbreviation (ex. MA) : ")

if state == "MA":
    comp = input("You're also from New England? Awesome! Did you enjoy talking to a computer? "
                 "(Please respond with 'yes' or 'no'): ")
elif state == "CT":
    comp = input("You're also from New England? Awesome! Did you enjoy talking to a computer? "
                 "(Please respond with 'yes' or 'no'): ")
elif state == "ME":
    comp = input("You're also from New England? Awesome! Did you enjoy talking to a computer? "
                 "(Please respond with 'yes' or 'no'): ")
elif state == "NH":
    comp = input("You're also from New England? Awesome! Did you enjoy talking to a computer? "
                 "(Please respond with 'yes' or 'no'): ")
elif state == "RI":
    comp = input("You're also from New England? Awesome! Did you enjoy talking to a computer? "
                 "(Please respond with 'yes' or 'no'): ")
elif state == "VT":
    comp = input("You're also from New England? Awesome! Did you enjoy talking to a computer? "
                 "(Please respond with 'yes' or 'no'): ")

"""This is just a very complicated way to determine if the user is from New England"""

else:
    comp = input("Cool! I'm from New England but " + state +
                 " also seems like a cool place. Did you enjoy talking to a computer? "
                 "(Please respond with 'yes' or 'no'): ")

if comp == "yes":
    print("I enjoyed talking to you as well " + name + "! Enjoy the rest of your day!")

elif comp == "no":
    print("I'm sorry " + name + "! You are welcome to edit my code if you would like to change anything. "
                                "Enjoy the rest of your day!")

else:
    print("Please respond with 'yes' or 'no' and try again")

"""this just wraps up the code and prints the line rather than making it an input question."""






