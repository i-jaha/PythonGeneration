'''
Обратный порядок 1
Дано натуральное число. 
Напишите программу, которая выводит его цифры в столбик в обратном порядке.
'''

n = int(input())
while n > 0:
    print(n % 10)
    n //= 10