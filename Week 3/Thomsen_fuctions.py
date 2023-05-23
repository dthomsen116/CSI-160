"""Must develop 3 of my own functions

Author:David Thomsen
Class: CSI-160
Assignment: Function Lab
Due Date: 9/23/21

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
#_______________________________________________________________________________________________________________________

def math(x,y):
    response = input("Would you like to add, subtract, multiply, or divide? (Please respond with (a/s/d/m)): ")


    if response == "a":
        return (int(x) + int(y))

    elif response == "s":
        return (int(x) - int(y))

    elif response == "d":
        return (int(x) / int(y))

    elif response == "m":
        return (int(x) * int(y))

    else:
        print("Invalid input, please try again.")
        math(x,y)

print("Your answer is " + str(math(1,3)) + ".")

"""
One sentence description: This function allows the user to do basic math functions 
between two numbers that they get to choose.

List of arguments with their usage:

x = The first number the user puts in
y = The second number the user puts in


Return value and it's usage:

The return values just do the proper math function and calculate the result.

Assumptions and conditions:

I am assuming that the user will put in numbers to add together as there is no failsafe if there is a wrong input, 
it will just go to a trace back error. 

There is an if/else conditional in this function that just reads the users input and decides what function is going to 
be used.

"""
#_______________________________________________________________________________________________________________________


def shaq(height_ft , weight_lbs):
    h_diff = 7.083 - int(height_ft)
    w_diff = 375 - int(weight_lbs)

    print ("You are " + str(h_diff) + " feet shorter than Shaq and weigh "
           + str(w_diff) + " pounds less than Shaq.")

shaq(6,180)

"""
One sentence description: This function tells the user how much shorter and how much less they weigh compared to 
Shaquille O'Neal.

List of arguments with their usage:

height_ft = the user's height in feet
weight_lbs = The user's weight in pounds


Return value and it's usage:

There is no return value as I was unable to get it to work with it. I will paste my original code so you can see the
attempt however I was unable to get it working that way. 

'''def shaq(height_ft , weight_lbs):
    return 7.1 - int(height_ft)
    return 375 - int(weight_lbs)

    print ("You are " + str(height_ft) + " feet shorter than Shaq and weigh "
           + str(weight_lbs) + " pounds less than Shaq.")



shaq(6 , 180)'''


Assumptions and conditions:

I am assuming that the users using this program are both shorter, and weigh less than Shaq. If they are not then the 
value will be negative and it will say "-1.2 feet shorter than Shaq...". I had tried to fix this using a conditional 
that checked the values of the height and weight however when it ran it had kept saying the values were not defined even
though those same vales work fine now. 

"""
#_______________________________________________________________________________________________________________________

num = 1

def cannot_equal_zero_but_always_equals_one(num):
    return (abs(num) - (abs(num) - 1))

if num != 1:
    print("Acceptable. Your result is 1")
else:
    print("Nope. Try again.")

#_______________________________________________________________________________________________________________________

"""
One sentence description: This function takes the num value and makes sure that the answer comes out to be one and
cannot be zero

List of arguments with their usage:

num = a number of the users choice that is put in the function and reduced to one. 


Return value and it's usage:

The return value takes the num value and subtracts all but one. It does the math for the function and determines the end
value of the function. 

Assumptions and conditions:

I am assuming the user will input a number value. If the user inputs a string there will be an error. 

The if/else conditional makes sure that the user puts in a value that is not one. If a one is entered than it will tell
the user that it is an unacceptable value and they must try it again.

"""















