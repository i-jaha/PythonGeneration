'''
Google search - 2
На вход программе подаются натуральное число n, 
затем n строк, 
затем число k – количество поисковых запросов, 
затем k строк – поисковые запросы. 
Напишите программу, которая выводит все введённые строки, 
в которых встречаются одновременно все поисковые запросы.
Поиск не должен быть чувствителен к регистру символов.
'''

n = int(input())
phrases = []
for i in range(n):
    phrases.append(input())
k = int(input())
searches = []
for i in range(k):
    searches.append(input())
for i in phrases:
    for j in searches:
        if j.lower() not in i.lower():
            break
    else:
        print(i)