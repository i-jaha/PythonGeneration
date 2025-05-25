'''
Без нулей 0️
Напишите программу, которая считывает 10 чисел и 
выводит произведение отличных от нуля чисел.
'''

product = 1
for i in range(10):
    n = int(input())
    if n != 0:
        product *= n
if product == 1:
    product = 0
print(product)