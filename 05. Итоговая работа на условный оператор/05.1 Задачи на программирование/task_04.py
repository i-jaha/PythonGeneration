'''
Римские цифры
Напишите программу, которая считывает целое число и 
выводит соответствующую ему римскую цифру. 
Если число находится вне диапазона [1;10], то 
программа должна вывести текст «ошибка» (без кавычек).
'''

number = int(input())
if 1<= number <= 10:
    if number == 1:
        print("I")
    elif number == 2:
        print("II")
    elif number == 3:
        print("III")
    elif number == 4:
        print("IV")
    elif number == 5:
        print("V")
    elif number == 6:
        print("VI")
    elif number == 7:
        print("VII")
    elif number == 8:
        print("VIII")
    elif number == 9:
        print("IX")
    elif number == 10:
        print("X")
else:
    print("ошибка")