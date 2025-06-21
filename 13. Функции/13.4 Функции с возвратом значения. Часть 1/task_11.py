'''
Merge lists 1
Напишите функцию merge(list1, list2), 
которая принимает в качестве аргументов два отсортированных по возрастанию списка, 
состоящих из целых чисел, и объединяет их в один отсортированный список.
Примечание 1. 
Можно использовать списочный метод sort(), а можно обойтись и без него. 😎
Примечание 2. 
Приведённый ниже код:
    print(merge([1, 2, 3], [5, 6, 7, 8]))
    print(merge([1, 7, 10, 16], [5, 6, 13, 20]))
должен выводить:
    [1, 2, 3, 5, 6, 7, 8]
    [1, 5, 6, 7, 10, 13, 16, 20]
Примечание 3.
list.sort() сортирует исходный список на месте, изменяет индексы списка и возвращает None
sorted() возвращает новый отсортированный список, оставляя исходный список без изменений.
'''

# example
# объявление функции
def merge(list1, list2):
    pass

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))



# review
def merge(list1, list2):
    new_list = list1 + list2
    return sorted(new_list)

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))