'''
Арифметические строки
Вводятся 3 строки в случайном порядке. 
Напишите программу, которая выясняет, 
можно ли из длин этих строк построить арифметическую прогрессию.
рограмма должна вывести строку «YES» (без кавычек), 
если из длин введённых слов можно построить арифметическую прогрессию, 
или «NO» (без кавычек) в противном случае.
'''

# option 1
a, b, c = input(), input(), input()
len_a, len_b, len_c = len(a), len(b), len(c)
if (len_a + len_c) / 2 == len_b or (len_b + len_c) / 2 == len_a or (len_a + len_b) / 2 == len_c:
    print("YES")
else:
    print("NO")

# option 2
len_1 = len(input())
len_2 = len(input())
len_3 = len(input())
if (2 * len_1 - len_2 - len_3) * (2 * len_2 - len_1 - len_3) * (2 * len_3 - len_1 - len_2) == 0:
    print('YES')
else:
    print('NO')