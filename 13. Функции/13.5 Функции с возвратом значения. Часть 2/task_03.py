'''
Is the Number Prime?
Напишите функцию is_prime(num), 
которая принимает в качестве аргумента натуральное число 
и возвращает значение True, если число является простым, 
или False в противном случае.
Примечание 1. 
Приведённый ниже код:
    print(is_prime(1))
    print(is_prime(10))
    print(is_prime(17))
должен выводить:
    False
    False
    True
Примечание 2. 
Простое число – это натуральное число, 
единственными делителями которого являются только оно само и 1.
Примечание 3. 
Число 1 простым не является.
'''

# # example
# # объявление функции
# def is_prime(num):
#     pass
# # считываем данные
# n = int(input())
# # вызываем функцию
# print(is_prime(n))



# review
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    if num > 1:
        return True
    else:
        return False
n = int(input())
print(is_prime(n))