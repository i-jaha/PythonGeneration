'''
Звёздный треугольник
а вход программе подаётся натуральное число n (n >= 2) 
– катет прямоугольного равнобедренного треугольника.
Напишите программу, которая выводит звёздный треугольник в соответствии с примером.
'''

n = int(input())
for i in range(n):
    print("*" * (n-i))