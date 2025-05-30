'''
Квадратное уравнение
Даны три действительных числа a, b, c.
Напишите программу, которая находит действительные корни квадратного уравнения.
Если уравнение имеет один корень, то нужно вывести его, 
а если уравнение имеет два корня, то следует вывести их в порядке возрастания, 
каждый на отдельной строке. 
При этом если уравнение не имеет действительных корней, 
то программа должна вывести текст «Нет корней» (без кавычек).
'''

from math import sqrt
a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - 4 * a * c
if D < 0:
    print("Нет корней")
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(x1)
    print(x2)