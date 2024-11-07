# Exercise 9: Hello

# This program defines a function that prints a simple greeting message and another function that calls on the previous function.
# When the program is run, it will print "Hello".

# This function displays the word "Hello" when called.
def hello():
    print("Hello")

# This function calls the hello function to display "Hello".
def main():
    hello()


# This checks if the program is being executed directly and is not imported as a module.
# If so, it will call the main function.
if __name__ == "__main__":
    main()
