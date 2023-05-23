
def is_hebrew_leap_year():

    year = int(input("Please enter the year: "))

    if year % 19 == 0:
        print("This year is not a leap year.")
    elif year % 19 == 3:
        print("This year is a leap year.")
    elif year % 19 == 6:
        print("This year is a leap year.")
    elif year % 19 == 8:
        print("This year is a leap year.")
    elif year % 19 == 11:
        print("This year is a leap year.")
    elif year % 19 == 14:
        print("This year is a leap year.")
    elif year % 19 == 17:
        print("This year is a leap year.")
    else:
        print("This is not a leap year.")
