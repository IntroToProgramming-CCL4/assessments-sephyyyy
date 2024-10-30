# Exercise 3: Biography

# Advanced Requirements:
user_name = input("What is your name?  ")
town = input("Where is your hometown?  ")
years = input("What's your age?  ")

user_name.split()
town.split()

user_info = {'name': [user_name],'hometown': [town],'age': years}
name = ' '.join(user_info['name'])
hometown = ' '.join(user_info['hometown'])
age = user_info ['age']
print (f"Hi {name}!")
print (f"According to your inputs, I know that you're {age} years old and your hometown is {hometown}.")
#print (user_info)

#Basic Requirements:
#personal_info = {'name': 'Joseph','hometown':'Cabadbaran','age':18}
#name = personal_info ['name']
#hometown = personal_info ['hometown']
#age = personal_info ['age']
#print (f"The users name is: {name}")
#print (f"Joseph's hometown is {hometown}")
#print (f"Joseph's is {age} years old.")