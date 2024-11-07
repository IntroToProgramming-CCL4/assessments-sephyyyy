# Exercise 8: Simple Search

# This program has a list of names and allows a user to search for a name in the list.
# If the name is or is not in the list, the program will inform the user, ending the program.

# This list contains the names that can be searched.
user_names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# This asks the user to enter a name and capitalizes the input so that it matches with the format of the contents of the list.
find = input("To check if a name is on the list, enter it here:  ").capitalize()

# This checks if the entered name can be found in the list of names.
if find in user_names:
    # If the name is found, it displays a message stating that it is in the list.
    print (f"The name {find} is in the list.")
else:
    # If the name is not found, it displays a message stating that it is not in the list.
    print (f"The name {find} is not in the list.")
