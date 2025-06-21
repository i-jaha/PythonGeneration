'''
Делители 2
Напишите функцию number_of_factors(num), 
принимающую в качестве аргумента число 
и возвращающую количество делителей данного числа.
Примечание 1. 
Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.
Примечание 2. 
Приведённый ниже код:
print(number_of_factors(1))
print(number_of_factors(5))
print(number_of_factors(10))
должен выводить:
1
2
4
'''

# example
# объявление функции
def number_of_factors(num):
    pass

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))



# review
def number_of_factors(num):
    return len([i for i in range(1, num // 2 + 1) if num % i == 0] + [num])

n = int(input())

print(number_of_factors(n))