'''
Начало столетия
Напишите программу, которая определяет, 
оканчивается ли год с данным номером на два нуля. 
Если год оканчивается, то выведите «YES» (без кавычек), 
иначе выведите «NO» (без кавычек).
'''

year = int(input())
if year % 100 == 0:
    print("YES")
else:
    print("NO")