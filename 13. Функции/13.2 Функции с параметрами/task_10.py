'''
Сумма цифр
Напишите функцию print_digit_sum(), 
которая принимает одно натуральное число num 
и выводит на печать сумму его цифр.
'''

# example
# объявление функции
def print_digit_sum(num):
    pass
# считываем данные
n = int(input())
# вызываем функцию
print_digit_sum(n)


# review
def print_digit_sum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print(sum)
n = int(input())
print_digit_sum(n)