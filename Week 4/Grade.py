
def grades():

    letter = int(input("Please enter your grade percentage: "))

    if letter >= 93:
        print("A")
    elif (letter >= 90) and (letter <= 92):
        print("A-")
    elif (letter >= 87) and (letter <= 89):
        print("B+")
    elif (letter >= 83) and (letter <= 86):
        print("B")
    elif (letter >= 80) and (letter <= 82):
        print("B-")
    elif (letter >= 77) and (letter <= 79):
        print("C+")
    elif (letter >= 73) and (letter <= 76):
        print("C")
    elif (letter >= 70) and (letter <= 72):
        print("C-")
    elif (letter >= 67) and (letter <= 69):
        print("D+")
    elif (letter >= 63) and (letter <= 66):
        print("D")
    elif (letter >= 60) and (letter <= 62):
        print("D-")
    elif letter < 60:
        print("F")
    else:
        print("incorrect input please try again")
        grades()
