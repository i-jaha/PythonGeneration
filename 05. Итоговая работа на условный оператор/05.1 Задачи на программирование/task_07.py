'''
Ход коня
Даны две различные клетки шахматной доски. 
Напишите программу, которая определяет, 
может ли конь попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки, 
потом для второй клетки. 
Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую, 
или «NO» в противном случае.
'''

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# option 1
if (((x1 - x2) == 2 or (x1 - x2) == -2) and (y1 - y2)**2 == 1) or ((x1 - x2)**2 == 1 and ((y1 - y2) == 2 or (y1 - y2) == -2)):
    print("YES")
else:
    print("NO")

# option 2
difference_product = (x1 - x2) * (y1 - y2)
if difference_product == 2 or difference_product == -2:
    print("YES")
else:
    print("NO")

# option 3
if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
    print("YES")
else:
    print("NO")