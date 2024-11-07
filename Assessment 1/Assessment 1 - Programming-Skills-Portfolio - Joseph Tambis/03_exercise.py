# Exercise 3: Biography

# This program asks the user for their name, hometown, and age, stores them in a dictionary, and then displays the information across three lines.

# The program starts by asking for three inputs and stores them in separate variables.
user_name = input("What is your name?  ")
town = input("Where is your hometown?  ")
years = input("What's your age?  ")

# This part splits any multiple-word inputs in 'user_name' and 'town' into a list.
user_name.split()
town.split()

# The dictionary 'user_info' is then created to store the inputs. 'user_name' and 'town' will be lists, while 'years' will be a string or integer.
user_info = {'name': [user_name],'hometown': [town],'age': years}

# Three new variables are created by calling values from the dictionary. 
# 'user_name' and 'town' are then joined using {' '.join} to combine list items into a string with spaces between the words.
name = ' '.join(user_info['name'])
hometown = ' '.join(user_info['hometown'])
age = user_info ['age']

# This line will then print the information in the dictionary on three separate lines using a single print() statement, ending the program.
print (f"Your name is {name}\nYour hometown is {hometown}\nYou're {age} years old")
