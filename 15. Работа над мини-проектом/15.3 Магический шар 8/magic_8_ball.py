'''
Magic Ball 8
Project Description:
Magic Ball 8 (Fortune Ball) is a humorous way to predict the future.
The program should ask the user to enter a certain question,
and then randomly generate an answer.

Project Components:
    Integers (int type);
    Variables;
    Data input/output (input() and print() functions);
    Conditional statements (if/elif/else);
    While loop;
    Infinite loop;
    Break and continue statements;
    Working with the random module to generate random numbers.

Answer Options
Traditionally, the Magic 8 Ball has 20 answers, which can be divided into four groups.
|Positive          |Tentatively Positive|Neutral                      |Negative                        |
|------------------|--------------------|-----------------------------|--------------------------------|
|It is certain     |I think so - yes    |Cannot predict now           |Don&#39;t even think about it   |
|It is decidedly so|Probably            |Ask again later              |My reply is no                  |
|Without a doubt   |Good prospects      |Better not tell you now      |According to my information - no|
|Definitely yes    |Signs point to yes  |Cannot be predicted right now|Prospects are not very good     |
|You may rely on it|Yes                 |Concentrate and ask again    |Very doubtful                   |

Notes
Note 1.
Inside the magic ball there is a container with dark liquid, for example, ink.
A 20-sided figure floats in the liquid, with one answer printed on each side.

Note 2.
A polyhedron with 20 faces is called an icosahedron.

Program title
Connect the random module;
Create a list of answers containing 20 potential responses (Certainly, Predetermined, etc.)

User Greeting
Display the text message:
'Hello World, I am a magic ball, and I know the answer to any question you have.'
Clarify the user's name;
Display the greeting words, for example, 'Hello Timur'.

Main program loop
Set up a loop that will ask the user for input;
Prompt the user to ask a question;
Use the choice() function to display a random answer,
passing the list "answers" as an argument;
Ask the user if they want to ask another question,
if yes, return to the main loop of the program,
if no, display the message
'Come back if you have any more questions!' and exit the program.
'''

import random

print('Hello World, I am a magic ball, and I know the answer to any question you have.')
user_name = input('What is your name? ')
print(f'Hello {user_name}')
print("Enter 'exit' to terminate the program.\n")

answers = [
    "It is certain", "It is decidedly so", "Without a doubt", "Definitely yes", "You may rely on it",
    "I think so - yes", "Probably", "Good prospects", "Signs point to yes", "Yes",
    "Cannot predict now", "Ask again later", "Better not tell you now", "Cannot be predicted right now", "Concentrate and ask again",
    "Don't even think about it", "My reply is no", "According to my information - no", "Prospects are not very good", "Very doubtful"
]

while True:
    question = input("Ask your question: ")
    answer = random.choice(answers)
    print(answer)
    
    continue_question = input("Would you like to ask another question? (yes/no): ")
    if continue_question.lower() != "yes":
        print("Come back if you have any questions!")
        break