'''
Численный треугольник 2
Дано натуральное число n. 
Напишите программу, 
которая печатает численный треугольник с высотой, 
равной n, в соответствии с примером:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
...
Используйте вложенный цикл for.
'''

# option 1
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i * (i - 1) // 2 + j, end=' ')
    print()

# option 2
n = int(input())
cur = 1
for i in range(n):
    for _ in range(i + 1):
        print(cur, end=" ")
        cur += 1
    print()