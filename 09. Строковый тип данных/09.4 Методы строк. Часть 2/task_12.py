'''
.com or .ru
На вход программе подаётся строка текста. 
Напишите программу, которая проверяет, 
что строка заканчивается подстрокой .com или .ru.
Программа должна вывести «YES» (без кавычек), 
если введённая строка заканчивается подстрокой .com или .ru, 
или «NO» (без кавычек) в противном случае.
'''

s = input().lower()
if s.endswith('.com') or s.endswith('.ru'):
    print('YES')
else:
    print('NO')