'''
Удалите нечётные индексы
На вход программе подаются натуральное число n, 
а затем n целых чисел. 
Напишите программу, 
которая создаёт из указанных чисел список, 
затем удаляет все элементы, 
стоящие по нечётным индексам, 
а затем выводит полученный список.
Программа должна вывести список в соответствии с условием задачи.
Используйте оператор del.
'''

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
del lst[1::2]
print(lst)