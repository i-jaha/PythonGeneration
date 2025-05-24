'''
Абсолютная сумма
Даны пять чисел a1, a2, a3, a4, a5. 
Напишите программу, которая вычисляет сумму их модулей ∣a1|+∣a2|+∣a3|+∣a4|+∣a5|.
'''

a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
absolute_sum = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
print(absolute_sum)