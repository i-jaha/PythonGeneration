'''
Делители-1
На вход программе подаются два натуральных числа a и b (a< b). 
Напишите программу, которая находит натуральное число из отрезка 
[a;b] (от a до b включительно) с максимальной суммой делителей. 
Если чисел с максимальной суммой делителей несколько, 
то искомым числом является наибольшее из них. 
Ваша программа должна выводить ответ в следующем формате:
<число с максимальной суммой делителей> <сумма делителей этого числа>
'''

# option 1
a, b = int(input()), int(input())
max_sum_divisors = 0
max_num = 0
for i in range(a, b + 1):
    sum_divisors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum_divisors += j
    if sum_divisors > max_sum_divisors or (sum_divisors == max_sum_divisors and i > max_num):
        max_sum_divisors = sum_divisors
        max_num = i
print(max_num, max_sum_divisors)

# option 2
a, b = int(input()), int(input())
mx_num = -1
mx_sum = -1
for cur_num in range(a, b + 1):
    cur_sum = 0
    for j in range(1, cur_num + 1):
        if cur_num % j == 0:
            cur_sum += j
    if cur_sum >= mx_sum:
        mx_num = cur_num
        mx_sum = cur_sum
        
print(mx_num, mx_sum)