'''
451 градус по Фаренгейту
У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». 
Напишите программу, которая определяет, 
какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.
Для получения градусов по Цельсию из градусов по Фаренгейту используйте формулу.
'''

temp_c = float(input())
temp_f = 5/9 * (temp_c - 32)
print(temp_f)