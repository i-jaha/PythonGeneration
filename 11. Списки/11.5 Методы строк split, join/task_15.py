'''
Добавь разделитель
На вход программе подаётся строка текста и строка-разделитель. 
Напишите программу, которая вставляет указанный разделитель 
между каждым символом введённой строки текста.
На вход программе подаются строка текста и строка-разделитель, 
каждая на отдельной строке.
Программа должна вывести текст в соответствии с условием задачи.
'''

text = input()
separator = input()
print(separator.join(text))