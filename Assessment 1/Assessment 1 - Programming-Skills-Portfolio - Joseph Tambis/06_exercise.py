# Exercise 6: Brute Force Attack

# This program asks the user to input a password and compares it to the correct password, the user is only given 5 attempts to enter the correct password.
# If the correct password is entered, it displays 'Correct password entered.'.
# If the wrong password is entered more times than the limit, it will display 'You had too many attempts, the authorities have been alerted!'

# These variables hold the correct password and sets the password attempts to 5.
correct_password = '12345'
password_attempts = 5

# The program enters a loop that runs until either the correct password is entered or the password attempts run out.
while password_attempts > 0:
    password = input("Enter password:  ")

    # If the password is correct, the program will inform the user by displaying a message and then ends the loop.
    if password == correct_password:
        print ("Correct password entered.")
        break
    else:
        # If the password is wrong, the number of attempts will decrease and a message is displayed to inform the user.
        password_attempts -= 1
        print (f"You entered the wrong password, you have {password_attempts} attemp(s) left.")

# If the user uses up all their attempts, a message is displayed stating that the authorities have been alerted.
if password_attempts == 0:
    print("You had too many attempts, the authorities have been alerted!")
