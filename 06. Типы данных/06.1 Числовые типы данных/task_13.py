'''
Сортировка трёх
Напишите программу, которая упорядочивает три числа от большего к меньшему.
'''

n1, n2, n3 = int(input()), int(input()), int(input())
min_num = min(n1, n2, n3)
max_num = max(n1, n2, n3)
mid_num = n1 + n2 + n3 - min_num - max_num
print(max_num, mid_num, min_num, sep='\n')