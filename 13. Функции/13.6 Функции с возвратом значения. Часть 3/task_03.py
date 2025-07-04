import math
'''
Площадь и длина 📏
Напишите функцию get_circle(radius), 
которая принимает в качестве аргумента радиус окружности 
и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.
Примечание 1. 
Длина окружности и площадь круга радиуса r вычисляются по формулам:
С=2πr, S=πr**2
Примечание 2. 
Для числа π используйте глобальную константу из модуля math.
Примечание 3. 
Приведённый ниже код:
    print(get_circle(1))
    print(get_circle(1.5))
должен выводить:
    6.283185307179586 3.141592653589793
    9.42477796076938 7.0685834705770345
'''

# # example
# # объявление функции
# def get_circle(radius):
#     pass

# # считываем данные
# r = float(input())

# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)




# review
from math import pi
def get_circle(radius):
    circle_length = 2 * pi * radius
    circle_square = pi * radius ** 2
    return circle_length, circle_square

r = float(input())

length, square = get_circle(r)
print(length, square)