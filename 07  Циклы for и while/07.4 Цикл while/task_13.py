'''
Количество пятёрок
На вход программе подаётся последовательность целых чисел от 1 до 5, 
характеризующее оценку ученика, каждое число на отдельной строке. 
Концом последовательности является любое неположительное число 
либо число, большее 5. 
Напишите программу, которая выводит количество пятерок.
'''

n = int(input())
count = 0
while n > 0 and n <= 5:
    if n == 5:
        count += 1
    else:
        count += 0
    n = int(input())
print(count)