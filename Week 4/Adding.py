
def two_numbers():

    num1 = int(input("Input a number: "))

    num2 = int(input("Input another number: "))

    if (num1 + num2) > 100:
        print("They add up to a big number")
    else:
        ans = (num1 + num2)
        print("They add up to " + str(ans))
