'''
Простые числа
На вход программе подается два натуральных числа a и b(a<b). 
Напишите программу, которая находит все простые числа от a до b включительно.
Программа должна вывести все простые числа от a до b включительно, 
каждое на отдельной строке.
Простое число – это натуральное число, 
единственными делителями которого являются только оно само и 1.
Число 1 простым не является.
'''

# option 1
a, b = int(input()), int(input())
if a < b:
    for i in range(a, b + 1):
        if i < 2:
            continue
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)

# option 2
a, b = int(input()), int(input())
for num in range(a, b + 1):
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)