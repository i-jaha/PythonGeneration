'''
Тимур и его числа 🌶️
Тимур загадал число от 1 до n (включительно), 
а Руслан собирается его отгадать. 
Каждый раз Руслан называет число Тимуру, 
а Тимур отвечает ему одним из способов: "больше", "меньше", "ты отгадал!". 
За какое наименьшее количество попыток Руслан может гарантированно угадать число Тимура?
На вход программе подаётся натуральное число n.
Программа должна вывести наименьшее количество попыток, 
которых гарантированно хватит Руслану, чтобы угадать число Тимура.
'''

# option 1
import math
n = int(input()) + 1
if n > 1:
    print(math.ceil(math.log2(n)))    
else:
    print(1)




# option 2
n = int(input())
attempts = 0
while n >= 2 ** attempts:
    attempts += 1
print(attempts)