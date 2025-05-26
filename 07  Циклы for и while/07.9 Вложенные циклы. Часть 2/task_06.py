'''
Сумма факториалов
Дано натуральное число n. 
Напишите программу, которая выводит значение суммы:
    1!+2!+3!+…+n!
Факториалом натурального числа n называется 
произведение всех натуральных чисел от 1 до n, то есть:
    n!=1⋅2⋅3⋅…⋅n
Задачу можно решить без вложенного цикла. Напишите две версии программы.
'''

# option 1
n = int(input())
factorial = 1
sum_factorials = 0
for i in range(1, n + 1):
    factorial *= i
    sum_factorials += factorial
print(sum_factorials)

# option 2
from math import factorial
n = int(input())
sum_factorials = 0
for i in range(1, n + 1):
    sum_factorials += factorial(i)
print(sum_factorials)

# option 3
n = int(input())
res = 0
for i in range(1, n + 1):
    cur_fact = 1
    for j in range(1, i + 1):
        cur_fact *= j
    res += cur_fact
print(res)