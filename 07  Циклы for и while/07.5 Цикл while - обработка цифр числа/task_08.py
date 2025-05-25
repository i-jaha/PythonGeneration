'''
Вторая цифра
Дано натуральное число n(n>9). 
Напишите программу, которая определяет его вторую (с начала) цифру.
'''

n = int(input())

# option 1
if n > 9:
    if n < 100:
        second_digit = n % 10
    else:
        n //= 10
        while n > 10:
            second_digit = n % 10
            n //= 10        
print(second_digit)

# option 2
while n > 99:
    n //= 10
second_digit = n % 10
print(second_digit)