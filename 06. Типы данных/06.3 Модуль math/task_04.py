'''
Средние значения
В математике выделяют следующие средние значения:
    среднее арифметическое чисел a и b
    среднее геометрическое чисел a и b
    среднее гармоническое чисел a и b
    среднее квадратичное чисел a и b
'''

from math import sqrt
a, b = float(input()), float(input())
arithmetic_mean = (a + b) / 2
geometric_mean = sqrt(a * b)
harmonic_mean = (2 * a * b) / (a + b)
quadratic_mean = sqrt((a ** 2 + b ** 2) / 2)
print(arithmetic_mean, geometric_mean, harmonic_mean, quadratic_mean, sep='\n')