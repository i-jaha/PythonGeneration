'''
Последовательность чисел 3
Даны два целых числа m и n (m>n).
Напишите программу, которая выводит все нечётные целые числа от m до n (включительно) 
в порядке убывания.
'''

m, n = int(input()), int(input())
if m > n:
    for i in range(m, n - 1, -1):
        if i % 2 != 0:
            print(i)