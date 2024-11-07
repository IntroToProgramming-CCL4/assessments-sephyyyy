# Exercise 7: Some Counting

# This program showcases different counting sequences by using for loops to print numbers in given ranges.
# The loops count in different ways (up, down, with steps) and display the results line by line.

# This loop counts from 0 to 50 and displays each number.
for number in range(0, 51):
    print(number)
print ("\n") # This prints a newline to separate each loop's output.

# This loop counts down from 50 to 0 and displays each number.
for number in range(50, -1, -1):
    print(number)
print ("\n")

# This loop counts from 30 to 50 and displays each number.
for number in range(30, 51):
    print(number)
print ("\n")

# This loop counts down from 50 to 10, in steps of 2, and displays each number.
for number in range(50, 9, -2):
    print(number)
print ("\n")

# This loop counts from 100 to 200, in steps of 5, and displays each number.
for number in range(100, 201, 5):
    print(number)
