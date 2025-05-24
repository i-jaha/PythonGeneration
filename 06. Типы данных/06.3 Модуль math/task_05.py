'''
Тригонометрическое выражение
Напишите программу, вычисляющую значение тригонометрического выражения
по заданному числу градусов x.
'''

from math import sin, cos, tan, radians
x = float(input())
x_rad = radians(x)
trig_expression = sin(x_rad) + cos(x_rad) + tan(x_rad) ** 2
print(trig_expression)