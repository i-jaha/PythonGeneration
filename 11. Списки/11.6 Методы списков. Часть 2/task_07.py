'''
Количество артиклей
На вход программе подаётся строка, содержащая английский текст. 
Напишите программу, которая подсчитывает общее количество артиклей: a, an, the.
На вход программе подаётся строка, содержащая английский текст. 
Слова текста разделены символом пробела.
Программа должна вывести общее количество артиклей a, an, the 
вместе с поясняющим текстом.
Артикли могут начинаться с заглавной буквы A, An, The.
'''

text = input().split()
count = 0
for i in text:
    if i.lower() in ['a', 'an', 'the']:
        count += 1
print(f"Общее количество артиклей: {count}")