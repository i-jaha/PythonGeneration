'''
Последовательность чисел 1
Даны два целых числа m и n (m <= n).
Напишите программу, которая выводит все целые числа от m до n включительно.
'''

m, n = int(input()), int(input())
for i in range(m, n + 1):
    print(i)