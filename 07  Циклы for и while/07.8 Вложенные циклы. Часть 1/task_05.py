'''
Таблица-1
Дано натуральное число n(n≤ 9). 
Напишите программу, которая печатает таблицу размером n×3, 
состоящую из данного числа (числа отделены одним пробелом).
Программа должна вывести таблицу размером n×3, состоящую из данного числа.
'''

n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()