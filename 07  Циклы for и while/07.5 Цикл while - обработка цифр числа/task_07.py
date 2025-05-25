'''
Все вместе
Дано натуральное число. 
Напишите программу, которая вычисляет:
    сумму его цифр;
    количество цифр в нем;
    произведение его цифр;
    среднее арифметическое его цифр;
    его первую цифру;
    сумму его первой и последней цифры.
'''

n = int(input())
sum = 0
count = 0
product = 1
average = 0
first_digit = n
last_digit = n % 10

while n > 0:
    digit = n % 10
    sum += digit
    count += 1
    product *= digit
    n //= 10

if count > 0:
    average = sum / count

first_digit = first_digit
while first_digit >= 10:
    first_digit //= 10

result = first_digit + last_digit

print(sum)
print(count)
print(product)
print(average)
print(first_digit)
print(result)