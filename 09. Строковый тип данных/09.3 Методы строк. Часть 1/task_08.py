'''
Заглавные буквы
На вход программе подаётся строка, состоящая из имени и фамилии человека, 
разделённых одним пробелом. 
Напишите программу, которая проверяет, 
что имя и фамилия начинаются с заглавной буквы.
Программа должна вывести «YES» (без кавычек), 
если имя и фамилия начинаются с заглавной буквы, 
или «NO» (без кавычек) в противном случае.
'''

s = input()
if s == s.title():
    print('YES')
else:
    print('NO')