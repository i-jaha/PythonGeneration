'''
Делители 1
Напишите функцию get_factors(num), 
принимающую в качестве аргумента натуральное число 
и возвращающую список всех делителей данного числа.
Примечание. 
Приведённый ниже код:
print(get_factors(1))
print(get_factors(5))
print(get_factors(10))
должен выводить:
[1]
[1, 5]
[1, 2, 5, 10]
'''

# example
# объявление функции
def get_factors(num):
    pass

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))



# review 1
def get_factors(num):
    divisors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
    divisors.append(num)
    return divisors

n = int(input())

print(get_factors(n))



# review 2
def get_factors(num):
    return [i for i in range(1, num // 2 + 1) if num % i == 0] + [num]

n = int(input())

print(get_factors(n))