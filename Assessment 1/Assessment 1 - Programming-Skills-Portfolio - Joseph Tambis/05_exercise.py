# Exercise 5: Days of the Month

# This program informs the user on the number of days a month has by asking the user to input the month number.
# This program also accounts for leap year as it changes the number of days February has.

# This dictionary has the month numbers as keys and the values are the number of days in those months.
# February which is '2' has a list as it's value to account for leap years.
months = {1: 31,
          2: [28, 29], # February has a different number of days depending if it's a leap year or not.
          3: 31,
          4: 30,
          5: 31,
          6: 30,
          7: 31,
          8: 31,
          9: 30,
          10: 31,
          11: 30,
          12: 31}

# This prints an introduction to what the program will do.
print("This program will tell you how many days a month has after you input that month's number.")

# This asks the user to enter the month number.
query = int(input("Please input the month number here:  "))

# This checks if the input month is valid
if query > 0 and query <= 12:

    # This checks if the user's input is February's month number.
    if query == 2:
        # If the user inputs February's month number, this will ask the user if it's a leap year or not.
        leap_year = input ("Is the year a leap year? (yes/no) ").lower()

        # This will then display the number of days February has after checking the answer to the last question.
        if leap_year == "yes":
            print(f"That month has {months[query][1]} days.")
        else:
            print(f"That month has {months[query][0]} days.")

    else:
        # For other months, this displays the number of days right away.
        print(f"That month has {months[query]} days.")

else:
    # If an invalid month number was provided, it will print this error message.
    print('No month matches your input number.')
