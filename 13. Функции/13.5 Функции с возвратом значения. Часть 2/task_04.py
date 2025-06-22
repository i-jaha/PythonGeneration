'''
Next Prime
Напишите функцию get_next_prime(num), 
которая принимает в качестве аргумента натуральное число num 
и возвращает первое простое число, большее числа num.
Примечание 1. 
Используйте функцию is_prime() из предыдущей задачи.
Примечание 2. 
Приведённый ниже код:
    print(get_next_prime(6))
    print(get_next_prime(7))
    print(get_next_prime(14))
должен выводить:
    7
    11
    17
'''

# # example
# # объявление функции
# def get_next_prime(num):
#     pass
# # считываем данные
# n = int(input())
# # вызываем функцию
# print(get_next_prime(n))



# review
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    if num > 1:
        return True
    else:
        return False

def get_next_prime(num):
    candidate = num + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

n = int(input())

print(get_next_prime(n))