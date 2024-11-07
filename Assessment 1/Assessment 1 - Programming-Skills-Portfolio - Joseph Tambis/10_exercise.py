# Exercise 10: Is it even?

# This program asks the user to enter a number and determines if the number is positive, negative, even, odd, or zero.
# It then prints a message based on the input number, informing the user if their number is positive, negative, even, odd, or zero.

# The main function asks the user to input a number.
# The input number is then passed to the sub function which determines if the value is even or odd and if it is positive, negative, or zero.
# The sub function returns the corresponding message, which is then printed by the main function
def main():
    num = int(input("Input a number: "))
    message = sub(num)
    print (message)

# This function checks if the number is even or odd and if it is positive, negative, or zero.
# For each scenario, this function returns a corresponding message that will be displayed.
def sub(num):
    if (num%2) == 0 and num>0:
        return "Your number is positive even."
    elif (num%2) == 0 and num<0:
        return "Your number is negative even."
    elif (num%2) != 0 and num>0:
        return "Your number is positive odd."
    elif (num%2) != 0 and num<0:
        return "Your number is negative odd"
    else:
        return "Your number is zero."

# This checks if the program is being executed directly and is not imported as a module.
# If so, it will call the main function.  
if __name__ == "__main__":
    main()
