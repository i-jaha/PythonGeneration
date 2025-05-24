'''
Пол и потолок
Напишите программу, которая принимает на вход действительное число x 
и вычисляет по нему значение:
пол числа + потолок числа
'''

from math import floor, ceil
x = float(input())
result = floor(x) + ceil(x)
print(result)