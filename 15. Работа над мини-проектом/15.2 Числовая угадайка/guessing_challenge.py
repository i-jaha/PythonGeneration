"""
Number Guessing Game
Project Description:
The program generates a random number in the range from 1 to 100
and asks the user to guess this number.
If the user's guess is higher than the random number,
the program should display the message 'Too high, try again'.
If the guess is lower than the random number,
the program should display the message 'Too low, try again'.
If the user guesses the number correctly,
the program should congratulate them and display the message 
'You guessed it, congratulations!'.

Project components:
    - Integers (int type);
    - Variables;
    - Data input/output (input() and print() functions);
    - Conditional operator (if/elif/else);
    - While loop;
    - Infinite loop;
    - Break and continue operators;

Program Title
Connect the random module;
Generate a random number from 1 to 100;
Display the welcome message to the user: 'Welcome to the Number Guessing Game'

Validation function for input data
A user may potentially enter incorrect data,
for example, a non-numeric value or a number exceeding 100.
It's important to account for such cases to ensure the program continues to operate correctly.
Handling such situations is referred to as "foolproofing" (or "idiot-proofing").
Write a function called is_valid() that takes one string argument.
The function returns True
if the passed argument is an integer between 1 and 100 inclusive,
and False otherwise.

Main program loop
Organize a loop that will request data from the user
(the loop can be infinite (while True)
or it can use a flag variable which changes its state after the number is guessed);
Prompt the user for a number between 1 and 100;
Check the entered data using the is_valid() function:
if the data is incorrect, display the message: 'Maybe we should enter an integer between 1 and 100?' and proceed to the next iteration of the main loop;
if the data is correct, convert it to an integer for convenience in further processing.

Comparison of the entered number with the guessed number
Implement the comparison between the entered number and the guessed number:
If the entered number is less than the guessed number,
display the message: 'Your number is smaller than the guessed one. Try again.'
If the entered number is greater than the guessed number,
display the message: 'Your number is greater than the guessed one. Try again.'
If the entered number equals the guessed number,
display the message: 'You guessed it, congratulations!'
Display a farewell message to the user:
'Thank you for playing the number guessing game. See you again...'

Project Improvements
Add a counter for the number of attempts made by the user.
Once the number is guessed, the program should display the total number of attempts;
Add the ability to generate a new number (start a new game) after the user has correctly guessed the number;
Add the option to specify the upper limit for random number generation (from 1 to n).
"""

import random


def is_valid(s, max_num):
    try:
        num = int(s)
        return 1 <= num <= max_num
    except ValueError:
        return False


print("Welcome to the Number Guessing Game")

while True:
    max_number = int(input("Enter the right boundary for guessing the number: "))
    print(f"I made up a number from 1 to {max_number}. Try to guess it!")

    random_number = random.randint(1, max_number)
    attempts = 0

    while True:
        user_input = input("Enter your number: ")

        if not is_valid(user_input, max_number):
            print(f"But maybe we should still enter an integer from 1 to {max_number}?")
            continue

        user_guess = int(user_input)
        attempts += 1

        if user_guess < random_number:
            print("Your number is less than the one I guessed, try again")
        elif user_guess > random_number:
            print("Your number is greater than the guessed one, try again")
        else:
            print(f"You guessed it, congratulations! Number of attempts: {attempts}")
            break

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("Thank you for playing the number guessing game. See you again...")
