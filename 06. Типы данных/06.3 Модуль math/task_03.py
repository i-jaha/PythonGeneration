'''
Площадь и длина
Напишите программу, определяющую площадь круга и длину окружности по заданному радиусу R
'''

from math import pi
r = float(input())
area = pi * r ** 2
length = 2 * pi * r
print(area)
print(length)