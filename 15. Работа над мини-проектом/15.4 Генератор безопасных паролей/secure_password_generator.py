'''
Генератор безопасных паролей
Описание проекта: 
программа генерирует заданное количество паролей 
и включает в себя умную настройку на длину пароля, 
а также на то, какие символы требуется в него включить, 
а какие исключить.

Составляющие проекта:
    Целые числа (тип int);
    Переменные;
    Ввод / вывод данных (функции input() и print());
    Условный оператор (if/elif/else);
    Цикл for;
    Написание пользовательских функций;
    Работа с модулем random для генерации случайных чисел.

Заголовок программы
Подключите модуль random;
Создайте строковые константы:
    digits: 0123456789;
    lowercase_letters: abcdefghijklmnopqrstuvwxyz;
    uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
    punctuation: !#$%&*+-=?@^_.
Создайте переменную chars = '', 
которая будет содержать все символы, 
которые могут быть в генерируемом пароле.

Считывание пользовательских данных
Программа должна запрашивать у пользователя следующую информацию:
    Количество паролей для генерации;
    Длину одного пароля;
    Включать ли цифры 0123456789?
    Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
    Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
    Включать ли символы !#$%&*+-=?@^_?
    Исключать ли неоднозначные символы il1Lo0O?

Настройка генерируемых паролей
На основании введенной пользователем информации, 
сформируйте переменную chars, содержащую все символы, 
которые могут быть в генерируемом пароле.

Генерации пароля
Напишите функцию generate_password(), 
которая принимает два аргумента:
    length: длину пароля;
    chars: алфавит из символов которого состоит пароль;
и возвращает пароль.
Используя цикл for, сгенерируйте необходимое количество паролей.
'''

import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''

count = int(input('Количество паролей для генерации: '))
length = int(input('Длина одного пароля: '))
use_digits = input('Включать ли цифры 0123456789? (y/n): ').lower() == 'y'
use_uppercase = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ').lower() == 'y'
use_lowercase = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n): ').lower() == 'y'
use_punctuation = input('Включать ли символы !#$%&*+-=?@^_? (y/n): ').lower() == 'y'
exclude_ambiguous = input('Исключать ли неоднозначные символы il1Lo0O? (y/n): ').lower() == 'y'

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