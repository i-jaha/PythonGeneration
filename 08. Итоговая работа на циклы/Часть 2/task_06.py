'''
Все вместе 2
Дано натуральное число. 
Напишите программу, которая вычисляет:
    - количество цифр 3 в нём;
    - сколько раз в нём встречается последняя цифра;
    - количество чётных цифр;
    - сумму его цифр, больших пяти;
    - произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, 
    если такая цифра одна, то вывести её);
    - сколько раз в нём встречаются цифры 0 и 5 (всего суммарно).
Программа должна вывести значения указанных величин в указанном порядке, 
каждую на отдельной строке.
'''

n = int(input())
count_3 = 0
count_last_digit = 0
last_digit = n % 10
count_even = 0
sum_greater_than_5 = 0
product_greater_than_7 = 1
count_0_and_5 = 0
while n > 0:
    digit = n % 10
    if digit == 3:
        count_3 += 1
    if digit == last_digit:
        count_last_digit += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sum_greater_than_5 += digit
    if digit > 7:
        product_greater_than_7 *= digit
    if digit == 0 or digit == 5:
        count_0_and_5 += 1
    n //= 10
print(count_3)
print(count_last_digit)
print(count_even)
print(sum_greater_than_5)
print(product_greater_than_7)
print(count_0_and_5)