'''
Merge lists 2
На вход программе подаются число n, а затем n строк, 
содержащих целые числа в порядке возрастания. 
Из данных строк формируются списки чисел. 
Напишите программу, которая объединяет указанные списки в один отсортированный список 
с помощью функции quick_merge(), а затем выводит его.
На вход программе подаются натуральное число n, а затем n строк, 
содержащих целые числа в порядке возрастания, разделённые символом пробела.
Программа должна вывести элементы окончательного отсортированного списка каждое через пробел.
'''

def quick_merge(list1, list2):
    result = []

    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]
    
    return result

n = int(input())

res = [int(num) for num in input().split()]

for _ in range(n - 1):
    cur_list = [int(num) for num in input().split()]
    
    res = quick_merge(res, cur_list)

print(*res)