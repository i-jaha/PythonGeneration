'''
Secure Password Generator
Project Description:
The program generates a specified number of passwords 
and includes smart settings for password length, 
as well as options to include certain characters and exclude others.

Project components:
    Integers (int type);
    Variables;
    Data input/output (input() and print() functions);
    Conditional operator (if/elif/else);
    For loop;
    Writing custom functions;
    Working with the random module to generate random numbers.

Program Title
Connect the random module;
Create string constants:
    digits: 0123456789;
    lowercase_letters: abcdefghijklmnopqrstuvwxyz;
    uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
    punctuation: !#$%&*+-=?@^_.
Create a variable chars = '',
which will contain all characters
that may be present in the generated password.

User data input
The program should request the following information from the user:
    The number of passwords to generate;
    The length of one password;
    Should digits 0123456789 be included?
    Should uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ be included?
    Should lowercase letters abcdefghijklmnopqrstuvwxyz be included?
    Should symbols !#$%&*+-=?@^_ be included?
    Should ambiguous characters il1Lo0O be excluded?

Password Generation Settings
Based on the information entered by the user,
create a variable "chars" containing all the characters
that can be included in the generated password.

Password Generation
Write a function generate_password()
that takes two arguments:
    length: the length of the password;
    chars: the alphabet (set of characters) from which the password is made;
and returns a password.
Using a for loop, generate the required number of passwords.
'''

import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''

count = int(input('Number of passwords to generate: '))
length = int(input('Length of one password: '))
use_digits = input('Include digits 0123456789? (y/n): ').lower() == 'y'
use_uppercase = input('Include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ').lower() == 'y'
use_lowercase = input('Include lowercase letters abcdefghijklmnopqrstuvwxyz? (y/n): ').lower() == 'y'
use_punctuation = input('Include the characters !#$%&*+-=?@^_? (y/n): ').lower() == 'y'
exclude_ambiguous = input('Exclude ambiguous characters il1Lo0O? (y/n): ').lower() == 'y'

if use_digits:
    chars += digits
if use_uppercase:
    chars += uppercase_letters
if use_lowercase:
    chars += lowercase_letters
if use_punctuation:
    chars += punctuation

if exclude_ambiguous:
    for char in 'il1Lo0O':
        chars = chars.replace(char, '')
def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

for i in range(count):
    password = generate_password(length, chars)
    print(password)