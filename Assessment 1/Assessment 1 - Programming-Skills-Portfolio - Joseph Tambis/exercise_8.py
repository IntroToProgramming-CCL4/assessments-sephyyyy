# Exercise 8: Simple Search

user_names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
find = input("To check if a name is on the list, enter it here:  ").capitalize()

if find in user_names:
    print (f"The name {find} is in the list.")
else:
    print (f"The name {find} is not in the list.")