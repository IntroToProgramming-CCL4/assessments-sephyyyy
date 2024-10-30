# Exercise 6: Brute Force Attack

correct_password = '12345'
password_attempts = 5

while password_attempts > 0:
    password = input("Enter password:  ")
    if password == correct_password:
        print ("Correct password entered.")
        break
    else:
        password_attempts -= 1
        print (f"You entered the wrong password, you have {password_attempts} attemp(s) left.")
        
if password_attempts == 0:
    print("You had to many attempts, the authorities have been alerted!")
