'''
Negatives, Zeros and Positives
На вход программе подаются натуральное число n, 
а затем n целых чисел. 
Напишите программу, 
которая сначала выводит все отрицательные числа, 
затем нули, 
а затем все положительные числа, 
каждое на отдельной строке. 
Числа должны быть выведены в том же порядке, 
в котором они были введены.
'''

negatives = []
zeros = []
positives = []
n = int(input())    
for i in range(n):
    num = int(input())
    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeros.append(num)
    elif num > 0:
        positives.append(num)
print(*negatives, *zeros, *positives, sep='\n')