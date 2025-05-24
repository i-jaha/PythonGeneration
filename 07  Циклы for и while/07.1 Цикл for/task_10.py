'''
Популяция
На вход программе подаются три натуральных числа m, p, n:
    m: стартовое количество организмов;
    p: среднесуточное увеличение в %;
    n: количество дней для размножения.
Напишите программу, которая предсказывает размер популяции организмов 
с 1-го по n-й день (включительно). 
Программа должна выводить номер дня, а затем через пробел размер популяции в этот день.
'''

# option 1
m, p, n = int(input()), int(input()), int(input())
for i in range(1, n+1):
    s = (1 + p / 100) ** (i-1) * m
    print(i, s)

# option 2
m, p, n = int(input()), int(input()), int(input())
cur_population = float(m)
for i in range(n):
    print(i + 1, cur_population)
    cur_population = cur_population * (1 + p / 100)

# option 3
m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    cur_population = m * (1 + p / 100) ** i
    print(i + 1, cur_population)