# Exercise 4: Primitive Quiz

# This part of the program gives the variable 'score', an initial value of 0.
score = 0
# This set of code is needed for every question, so I placed it in this function to simplify and shorten the program.
def question(item_num, country, correct_answer):
     global score
     item_num = input (f"What is the capital of {country}? ").lower()
     if item_num == correct_answer:
          print ("Good job, your answer is correct!")
          score += 1
     else:
           print ("Your answer is sadly wrong.")
# This part of the program uses a while loop to repeatedly ask a user if they want to start the quiz until they type 'yes'.
start = input("You are now about to start a quiz on capital cities around Europe, please type yes to start the quiz:  ").lower()
while start != "yes":
     print("The quiz has not started.")
     start = input("Would you like to start now?  ")
else:
     print("The quiz has started.")
# This part of the program calls the function 'question' repeatedly to ask each question of the quiz.
question(1, "France", "paris")
question(2, "Greece", "athens")
question(3, "Ukraine", "kiev")
question(4, "Italy", "rome")
question(5, "Belgium", "brussels")
question(6, "Serbia", "belgrade")
question(7, "Spain", "madrid")
question(8, "United Kingdom", "london")
question(9, "Denmark", "copenhagen")
question(10, "Austria", "vienna")
# This part of the program prints a message giving the users quiz score using an f-string for string concantenation.
print(f"You got a score of: {score}/10")
# This part of the program uses if-else statements to determine what the code will say to the user based on their final score.
if score == 9 or score == 10:
     print("You are a geography wizz!")
elif score == 7 or score == 8:
     print("You know your stuff!")
else:
     print("Thank you for taking the quiz.")